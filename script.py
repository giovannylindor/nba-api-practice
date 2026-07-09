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
    parser.add_argument('-ll', nargs=1, help="Fetches the League Leader in a Specific Stat." \
    "\nFor Points, ENTER: PPG\nFor Assists, " \
    "ENTER: AST\nFor Rebounds, ENTER: REB")
    args = parser.parse_args()
    
    if args.p:
        get_player(args)
        
    if args.ll:
        get_league_leader(args)


def get_league_leader(args):
    """Fetches the league leader"""
    try:
        if args.p == 'pts':
            f = io.StringIO()
            with redirect_stdout(f):            
                leader = api.nba.leaders.get(stat_type='pts', season=2023)
        
            player = leader.data[0]
            print(f"The League Leader in Points is {player}")
    except (UnboundLocalError, IndexError):
        print("Cannot Find Player!")







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