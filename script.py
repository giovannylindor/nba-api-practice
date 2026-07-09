import argparse
from balldontlie import BalldontlieAPI
import os
import sys 
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
    player_info = api.nba.players.list(first_name=first_name)
    print(player_info) 


parse()