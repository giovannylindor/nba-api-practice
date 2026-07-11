import argparse
from balldontlie import BalldontlieAPI
import os
import io
from contextlib import redirect_stdout
from dotenv import load_dotenv

load_dotenv()
api = BalldontlieAPI(os.getenv("BALLDONTLIE_API"))
 

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs='+', help='Fetches a Players General Information')
    parser.add_argument('--t',  action='store_true', help="Fetches all 30 NBA Teams")
    args = parser.parse_args()
    
    if args.p:
        get_player(args)
        
    if args.t:
        get_all_teams(args)


def get_all_teams(args):
    """Fetches all 30 nba teams"""
    try:
        teams = [ ]
        all_teams_response = api.nba.teams.list()
        formatted_teams = all_teams_response.data[0:30]
        
        for t in formatted_teams:
            teams.append(t.full_name)

        for team in teams:
            print(team)
        

    except (IndexError, UnboundLocalError):
        pass
    





def get_player(args):
    """Fetches General Player Information"""

    # silences the json object returned from the api call 
    try:
        if len(args.p) == 1:
            first_name = args.p[0]
            f = io.StringIO()
            with redirect_stdout(f):
                player_query = api.nba.players.list(first_name=first_name)
            player = player_query.data[0]
        else:
            first_name = args.p[0]
            last_name = args.p[1]
            f = io.StringIO()
            with redirect_stdout(f):
                player_query = api.nba.players.list(first_name=first_name, last_name=last_name)
            player = player_query.data[0]

        print(f"Name: {player.first_name} {player.last_name}"
          f"\nPosition: {player.position}"
          f"\nHeight: {player.height}"
          f"\nWeight: {player.weight}"
          f"\nCollege: {player.college}"
          f"\nTeam: {player.team.full_name}")

    except (UnboundLocalError, IndexError):
        print("Cannot Find Player!")

    



parse()