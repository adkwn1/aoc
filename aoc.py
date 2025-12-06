#!/usr/bin/python3
# edit the line above to the appropriate path if required

import os
import argparse
import requests
import stat
from requests.exceptions import ConnectionError
from pathlib import Path
from dotenv import load_dotenv


def build_workspace(day:int, year:int):
    load_dotenv()
    uri = 'http://adventofcode.com/{year}/day/{day}/input'.format(year=year, day=day)
    dirpath = Path(f"./{year}/d_{day}/")
    dirpath.mkdir(parents=True, exist_ok=True)
            
    try:
        response = requests.get(uri, cookies={'session': os.getenv("SESSION_ID")}, headers={'User-Agent': os.getenv("USER_AGENT")})
                
    except ConnectionError as e:
        print(f"Connection error -- check uri, SESSION_ID and/or USER_AGENT variable(s): {repr(e)}")
    
    text = response.text if response.status_code == 200 else ""
    with open(f"./{str(dirpath)}/input.txt", "w") as input_file, open(f"./{str(dirpath)}/day_{day}.py", "w") as solution_file:
        input_file.write(text)
        solution_file.write(f'''#!/usr/bin/python3
# edit the line above to the appropriate path if required
                                                     
def solve():
    pass

                            
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        for line in file:
            print(line.strip())
    
    solve()\n''')
    
    f = Path(f"./{str(dirpath)}/day_{day}.py")
    f.chmod(f.stat().st_mode | stat.S_IEXEC)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Builds a workspace for the specified day's AoC problem with boilerplate files.")
    parser.add_argument("day", type=int, help="The specific AoC day (i.e. 1-25).")
    parser.add_argument("year", type=int, help="The specific AoC year (e.g. 2025).")

    args = parser.parse_args()
   
    build_workspace(args.day, args.year)
    