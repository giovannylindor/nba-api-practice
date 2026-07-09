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
    parser.add_argument('-p', nargs=2, help='Fetches a Players General Information')
    args = parser.parse_args()
    
    if args.p:
        get_player(args)
        

def get_player(args):
    first_name = args.p[0]
    last_name = args.p[1]
    
    # silences the json object returned from the api call 
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            player_query = api.nba.players.list(first_name=first_name, last_name=last_name)
        player = player_query.data[0] 
    except UnboundLocalError:
        print("Cannot Find Player!")

    

    print(f"Name: {player.first_name} {player.last_name}"
          f"\nPosition: {player.position}"
          f"\nHeight: {player.height}"
          f"\nWeight: {player.weight}"
          f"\nCollege: {player.college}"
          f"\nTeam: {player.team.full_name}")




parse()