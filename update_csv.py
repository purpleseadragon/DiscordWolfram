import pandas as pd
from prettytable import PrettyTable

indexes= {"oscar": 0, "roan": 1, "khy": 3, 
"leo": 4, "sam": 5, "zach": 6, "liam": 7, "zeke": 8}

def update_elos(team_winners, team_losers, team_win_delta, team_lose_delta):
    df = pd.read_csv("elos.csv")
    for player in team_winners:
        df.loc[indexes[player], ["Elo"]] += team_win_delta
    for player in team_losers:
        df.loc[indexes[player], ["Elo"]] += team_lose_delta
    df.to_csv("elos.csv",index=False)

def team_elos(team1, team2):
    """returns the elos for each player in team1 and team2"""
    team1_elos, team2_elos = [], []
    df = pd.read_csv("elos.csv", index_col='Player')
    for player in team1:
        elo = df.loc[player, 'Elo']
        team1_elos.append(elo)
    for player in team2:
        elo = df.loc[player, 'Elo']
        team2_elos.append(elo)
    return team1_elos, team2_elos


def print_leaderboard():
    leaderboard = PrettyTable()
    leaderboard.field_names = ["Player", "Elo"]
    with open('elos.csv') as f:
        next(f)
        line = f.readline()
        while line:
            leaderboard.add_row(line.rstrip().split(','))
            line = f.readline()
    return leaderboard

if __name__ == '__main__':
    #updatecsv(237337567534514176)
    print(team_elos(["oscar", "leo"], ["roan", "khy"]))
    update_elos(["oscar", "leo"], ["roan", "khy"], 5, -6)
    #print(print_leaderboard())
