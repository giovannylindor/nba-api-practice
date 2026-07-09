import argparse
from balldontlie import BalldontlieAPI
import os
from dotenv import load_dotenv

load_dotenv()


api = BalldontlieAPI(os.getenv("BALLDONTLIE_API"))
print(api.nba.teams.list())

