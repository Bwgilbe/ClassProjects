
import random
from collections import defaultdict
from itertools import combinations, permutations
import copy
import pandas as pd
import numpy as np

amount_teams = []

def style_matchups(df):
    return df.style.set_properties(**{'text-align': 'center'}).set_table_styles(
        [{'selector': 'th', 'props': [('text-align', 'center')]}]
    ).map(lambda x: 'background-color: lightyellow' if isinstance(x, list) else '')


while True:
    default = input("Do you want do default or choose the team names?\n")
    if default.lower() == "default":
        amount_teams = ["Team " + str(x + 1) for x in range(16)]
        break
    if default.lower() == "choose":
        while True:
            amount_teams.append(input(f"Please type the name of the team you wish to enter\n"))

            print("The list has been updated")
            print(amount_teams)

            if len(amount_teams) == 16:
                break

        break
    else:
        print("Please choose one of the options")

while True:
    name = input(f"What game type do you want want to do?(divisional,conference,nonconference) \n")
    if name.lower() == "divisional":
        game_types = {"divisional": 4, "conference": 2, "non_conference": 2}
        break
    if name.lower() == "conference":
        game_types = {"divisional": 0, "conference": 4, "non_conference": 4}
        break
    if name.lower() == "nonconference":
        game_types = {"divisional": 0, "conference": 0, "non_conference": 8}
        break
    if name.lower() != "divisional" or name.lower != "conference" or name.lower != "nonconference":
        print("Please type a valid option")

random.shuffle(amount_teams)

divisions = defaultdict(list)
for i, team in enumerate(amount_teams):
    divisions[i // 4].append(team)

conferences = defaultdict(list)
conference_nums = []
for division, teams in divisions.items():
    division_num = division // 2
    conferences[division_num] += teams
    conference_nums.append(division_num)

game_types_per_week = []
for k, v in game_types.items():
    game_types_per_week += [k] * v
random.shuffle(game_types_per_week)


def Matches_(all_teams_, All_matches_):
    All_matches_ = copy.deepcopy(All_matches_)
    weekly_teams_playing = set()
    weekly_matchups = []
    teams_remaining = set(all_teams_)

    while teams_remaining:
        team_1 = teams_remaining.pop()
        possible_teams = list(set(All_matches_[team_1]) - weekly_teams_playing)
        team_2 = random.choice(possible_teams)
        All_matches_[team_1].remove(team_2)
        All_matches_[team_2].remove(team_1)

        weekly_teams_playing = weekly_teams_playing.union(set([team_1, team_2]))
        weekly_matchups.append([team_1, team_2])
        teams_remaining.remove(team_2)
        ##print(weekly_matchups)
        ##print()
    return weekly_matchups


div_opponent = {}
con_opponent = {}
noncon_opponent = {}

for division, teams in divisions.items():
    for team in teams:
        div_opponent[team] = list(set(teams) - set([team])) * 2

for conference, teams in conferences.items():
    for team in teams:
        con_opponent[team] = list(set(teams) - set([team]) - set(div_opponent[team]))

        noncon_opponent[team] = copy.deepcopy(
            conferences[(conference + 1) % 2])

All_possible_matches = {"divisional": div_opponent, "conference": con_opponent, "non_conference": noncon_opponent, }
All_possible_matches['divisional']

weekly_teams_playing = defaultdict(set)
games_played = {}
weekly_matchups = []

for week, game_type in enumerate(game_types_per_week):

    matchups = None

    ATTEMPTS = 5000
    for attempt in range(ATTEMPTS):
        try:
            matchups = Matches_(amount_teams, All_possible_matches[game_type])
            break
        except:
            continue
    if not matchups:
        raise Exception(
            f"No valid matchups found for week {week} after {ATTEMPTS} attempts. Please check your settings are valid or try increasing the number of attempts")
    else:
        for name, All_possible in All_possible_matches.items():
            for team_1, team_2 in matchups:
                for a, b in permutations([team_1, team_2], 2):
                    if b in All_possible.get(a, []):
                        All_possible_matches[name][a].remove(b)

        weekly_matchups.append(matchups)

[x[0] for x in weekly_matchups]

N = len(amount_teams)
occurences_matrix = np.zeros((N, N))

for weeks_matchups in weekly_matchups:

    for team_1, team_2 in weeks_matchups:
        for a, b in permutations([team_1, team_2], 2):
            occurences_matrix[amount_teams.index(a)][amount_teams.index(b)] += 1

matchups_df = pd.DataFrame(weekly_matchups).T
matchups_df.columns = [f"Week {x + 1}" for x in range(len(weekly_matchups))]
def style_matchups(df):
    return df.style.set_properties(**{'text-align': 'center'}).set_table_styles(
        [{'selector': 'th', 'props': [('text-align', 'center')]}]
    ).map(lambda x: 'background-color: lightyellow' if isinstance(x, list) else '')

styled_df = style_matchups(matchups_df)
styled_df
