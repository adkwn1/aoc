import os
import argparse
import requests
from dotenv import load_dotenv


def build_workspace(day:int, year:int, part:int):
    load_dotenv()
    uri = 'http://adventofcode.com/{year}/day/{day}/input'.format(year=year, day=day)
    
    try:
        response = requests.get(uri, cookies={'session': os.getenv("SESSION_ID")}, headers={'User-Agent': os.getenv("USER_AGENT")})

    except Exception as e:
        print(f"Workspace not created. Error getting problem input: {repr(e)}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Builds a workspace for the specified day's AoC problem with boilerplate files.")
    parser.add_argument("day", type=int, help="The specific AoC day (i.e. 1-25).")
    parser.add_argument("year", type=int, help="The specific AoC year (e.g. 2025).")
    parser.add_argument("-p", "--part", required=False, type=int, help="Optional -- desired problem input (i.e. part 1 or 2).")
    args = parser.parse_args()
   
    build_workspace(args.day, args.year, args.part)