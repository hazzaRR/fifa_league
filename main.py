import numpy as np
import pandas as pd
import os


def create_league(players, league_name):

    """ function that creates a league table, which takes in an array of players for the league and also the name of the league """

    CURRENT_PATH = os.getcwd()
    league_path = os.path.join(CURRENT_PATH, "leagues", league_name)


    try:
        os.mkdir(league_path)
        num_of_players = len(players)

        starting_values = np.zeros((num_of_players,), dtype=int)

        league_table = {'Players': players, 'Matches Played': starting_values, "Wins": starting_values,
        "Losses": starting_values, "Goals Scored": starting_values, "Goals Conceded": starting_values,
         "Goal Difference": starting_values, "Points": starting_values}

        league_table_df = pd.DataFrame(data=league_table)


        match_history = pd.DataFrame(columns = ['Player 1', 'Player 2', 'Player_1_goals', "Player_2_goals"])

        league_table_df.to_csv(os.path.join(league_path, "League_table.csv"), index=False)
        match_history.to_csv(os.path.join(league_path, "Match_history.csv"), index=False)

    except:
        print("League name already exists, please enter a different name")






def main():

    print("hello")


if __name__ == "__main__":
    main();
    create_league(["Harry", "Callum", "Jack", "Barns"], "11 Friends Road")