import argparse
from math import inf

parser = argparse.ArgumentParser()
#Game data
parser.add_argument('--map_length', type=int, default=30)
parser.add_argument('--change_rate', type=int, default=1)
parser.add_argument('--game_time', type=int, default=3000)
parser.add_argument('--obstacle', type=int, default=50)
#Agent data
parser.add_argument('--p', type=float, default=1)
parser.add_argument('--k', type=float, default=inf)
parser.add_argument("--reaction_strategy", default="blind_commitment", type=str)
#Hole data
parser.add_argument('--min_generation_time', type=int, default=60)
parser.add_argument('--max_generation_time', type=int, default=240)
parser.add_argument('--min_life', type=int, default=240)
parser.add_argument('--max_life', type=int, default=960)
parser.add_argument('--min_score', type=int, default=1)
parser.add_argument('--max_score', type=int, default=10)
#score影响因子


config = parser.parse_args()