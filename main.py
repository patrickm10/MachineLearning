import pandas as pd

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Creates a dataframe for the team stats
stats_df = pd.DataFrame(columns=['Team_Name', 'Wins', 'Losses', 'Ties', 'Win_PCT' 'Points_For', 'Points_Against'])

# Reads the CSV data into a dataframe
df_nfl = pd.read_csv('/Users/pmejia/PycharmProjects/SportsWinnerCalculator-ML/NFL_Team_Stats.csv')


# Gets the teams total points per game and
# divides them by the teams total games they played
# Returns the teams points per game
def checkPointsPerGame(team1, team2):
    return team2


# Takes the teams stats and compares them to the league stats
# to find where the teams position should be in the league
# Returns a list of the teams ranked in order with win percentage
def parseTeamStats(team1, league1):
    for team in league1:
        if team1['Win_PCT'] > team['Win_PCT']:
            team1[index] = team[index]
            team[index] = team[index] + 1
    return league1


# Compares the first team to the second team and ranks the
# higher team and puts it in the list
def compareTeamStats(team1, team2):

    return team2


# Inputs data into the teams current stats
# Returns the list of teams by stats
def inputTeamStats(team1, league1):
    return league1

# Features that could be implemented into this program:
# Parse scores and points data
# Predict Winner
# Predict Probability of win
# Stats calculator
# Live stat updates by user
#   This will require logistic regression using machine Learning
# Introducing new team to league


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hi, this is Pat! This is the sports calculator. This project was made by Patrick Mejia'
          'and the program takes a bunch of statistics from CSV files and calculates the '
          'probability of a team winning a game and potentially the scores associated to each game.')

    # Iterate through the NFL statistics
    for index, row in df_nfl.iterrows():
        team_name = str(row[0])
        team_wins = str(row[1])
        team_losses = str(row[2])
        team_ties = str(row[3])
        team_pct = str(row[4])
        team_points_for = str(row[5])
        team_points_against = str(row[6])
        team_win_streak = str(row[15])

        spartans = {'FC Spartans', 3, 1, 0, }
        parseTeamStats(spartans)

        stats_df = stats_df.append(
            {'Team_Name': team_name, 'Wins': team_wins, 'Losses': team_losses, 'Ties': team_ties,
             'Win_PCT': team_pct, 'Points_For': team_points_for,
             'Points_Against': team_points_against, 'Win_Streak': team_win_streak}, ignore_index=True)

    stats_df.to_csv('/Users/pmejia/PycharmProjects/SportsWinnerCalculator-ML/NFL_Results.csv')
    print(stats_df)
