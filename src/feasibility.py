"""Inspect the three downloaded StatsBomb match samples from the project root."""

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / 'data' / 'raw' / 'statsbomb'
RESULTS = ROOT / 'results'
SAMPLES = [
    ('Euro 2024', 55, 282, 3930166),
    ('World Cup 2022', 43, 106, 3857276),
    ('Euro 2020', 55, 43, 3788758),
]
ACTION_TYPES = {'Pass', 'Carry', 'Dribble', 'Shot', 'Ball Receipt*', 'Miscontrol'}


def read_json(path):
    with path.open(encoding='utf-8') as source:
        return json.load(source)


def valid_xy(value):
    return (isinstance(value, list) and len(value) >= 2
            and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in value[:2]))


def write_csv(name, rows):
    if not rows:
        raise ValueError(f'No data for {name}')
    with (RESULTS / name).open('w', encoding='utf-8', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    RESULTS.mkdir(exist_ok=True)
    summary, actions, fields = [], [], []
    for tournament, comp, season, match_id in SAMPLES:
        matches_path = RAW / 'matches' / str(comp) / f'{season}.json'
        events_path = RAW / 'events' / f'{match_id}.json'
        frames_path = RAW / 'three-sixty' / f'{match_id}.json'
        matches, events, frames = map(read_json, (matches_path, events_path, frames_path))
        match = next(m for m in matches if m['match_id'] == match_id)
        event_ids = [e.get('id') for e in events]
        frame_ids = [f.get('event_uuid') for f in frames]
        if None in event_ids or None in frame_ids:
            raise ValueError(f'Missing join identifier in match {match_id}')
        if len(set(event_ids)) != len(event_ids) or len(set(frame_ids)) != len(frame_ids):
            raise ValueError(f'Duplicate join identifier in match {match_id}')
        frame_by_id = {f['event_uuid']: f for f in frames}
        joined = [e for e in events if e['id'] in frame_by_id]
        event_id_set = set(event_ids)
        unmatched_frames = sum(f['event_uuid'] not in event_id_set for f in frames)
        visibility = []
        empty_frames = malformed_players = 0
        for frame in frames:
            players = frame.get('freeze_frame')
            if not isinstance(players, list):
                empty_frames += 1
                continue
            if not players:
                empty_frames += 1
            valid_players = [p for p in players if isinstance(p, dict) and valid_xy(p.get('location'))
                             and isinstance(p.get('teammate'), bool)]
            malformed_players += len(players) - len(valid_players)
            visibility.append((sum(p['teammate'] for p in valid_players),
                               sum(not p['teammate'] for p in valid_players)))
        row = dict(tournament=tournament, competition_id=comp, season_id=season,
                   match_count=len(matches), match_id=match_id,
                   home_team=match['home_team']['home_team_name'], away_team=match['away_team']['away_team_name'],
                   metadata_bytes=matches_path.stat().st_size, events_bytes=events_path.stat().st_size,
                   frames_bytes=frames_path.stat().st_size, events=len(events), frames=len(frames),
                   joined_events=len(joined), join_percent=round(100 * len(joined) / len(events), 2),
                   unmatched_frames=unmatched_frames,
                   adjacent_same_possession_pairs=sum(
                       a.get('possession') is not None and a.get('possession') == b.get('possession')
                       and a.get('period') == b.get('period') for a, b in zip(events, events[1:])),
                   adjacent_same_possession_pairs_both_360=sum(
                       a.get('possession') is not None and a.get('possession') == b.get('possession')
                       and a.get('period') == b.get('period') and a['id'] in frame_by_id and b['id'] in frame_by_id
                       for a, b in zip(events, events[1:])),
                   events_missing_location=sum(not valid_xy(e.get('location')) for e in events),
                   frames_missing_visible_area=sum(not isinstance(f.get('visible_area'), list) or len(f['visible_area']) < 6 for f in frames),
                   frames_missing_or_empty_freeze_frame=empty_frames, malformed_player_records=malformed_players,
                   mean_visible_teammates=round(sum(x for x, _ in visibility) / len(visibility), 2) if visibility else '',
                   mean_visible_defenders=round(sum(x for _, x in visibility) / len(visibility), 2) if visibility else '',
                   min_visible_defenders=min((x for _, x in visibility), default=''),
                   max_visible_defenders=max((x for _, x in visibility), default=''))
        summary.append(row)
        for action in sorted(ACTION_TYPES):
            selected = [e for e in events if e.get('type', {}).get('name') == action]
            with_frame = [e for e in selected if e['id'] in frame_by_id]
            with_position = [e for e in with_frame if valid_xy(e.get('location'))]
            with_defender = [e for e in with_position if any(
                isinstance(p, dict) and p.get('teammate') is False and valid_xy(p.get('location'))
                for p in frame_by_id[e['id']].get('freeze_frame', []) or [])]
            actions.append(dict(tournament=tournament, match_id=match_id, action=action,
                                events=len(selected), event_location=sum(valid_xy(e.get('location')) for e in selected),
                                joined_360=len(with_frame), joined_with_event_location=len(with_position),
                                joined_with_location_and_visible_defender=len(with_defender)))
        for record_type, records in [('event', events), ('360', frames),
                                     ('360_player', [p for f in frames for p in f.get('freeze_frame', []) if isinstance(p, dict)]),
                                     ('pass', [e['pass'] for e in events if isinstance(e.get('pass'), dict)]),
                                     ('carry', [e['carry'] for e in events if isinstance(e.get('carry'), dict)])]:
            types = defaultdict(Counter)
            for record in records:
                for key, value in record.items():
                    types[key][type(value).__name__] += 1
            for key, counts in sorted(types.items()):
                fields.append(dict(tournament=tournament, match_id=match_id, record_type=record_type,
                                   field=key, present=sum(counts.values()), total=len(records),
                                   types='; '.join(f'{k}:{v}' for k, v in sorted(counts.items()))))
        print(f"{tournament} | {row['home_team']} vs {row['away_team']} ({match_id}) | "
              f"matches {len(matches)} | events {len(events)} | frames {len(frames)} | "
              f"joined {len(joined)} ({row['join_percent']}%) | "
              f"mean visible teammates/defenders {row['mean_visible_teammates']}/{row['mean_visible_defenders']}")
    write_csv('feasibility_summary.csv', summary)
    write_csv('feasibility_actions.csv', actions)
    write_csv('feasibility_fields.csv', fields)
    print('Wrote results/feasibility_summary.csv, feasibility_actions.csv, feasibility_fields.csv')
    print('360 snapshots show visible players only; joined events and visible defenders do not validate disruption labels.')


if __name__ == '__main__':
    main()
