# Advent of Code Utility
This is a Python utility to create a workspace for an [Advent of Code](https://adventofcode.com/2025/about) problem.

## Usage
1. Clone this repository.
2. Create an .env file and populate the following variables:
```env
SESSION_ID=<cookie ID from your browser after logging into adventofcode.com>
USER_AGENT=<user agent string from your browser>
```
To get your session ID and user agent string, inspect the HTTP GET request header from your browser. For example, if using Firefox, press `ctrl` + `shift` + `i` and copy the values from:


3. Run the `aoc.py` script.
```shell
user@domain:~$/../aoc/python3 aoc.py <DAY> <YEAR>
```
If desired, edit the "shebang" to the location of your Python interpreter (e.g. if on Windows or using a venv) to run `aoc.py` as a script:
```shell
./aoc.py <DAY> <YEAR>
```
The script creates the following directory structure and files:
```
aoc/
|---<YEAR>/
    |---d_<DAY>/
        |---day_<DAY>.py
        |---input.txt
```
For example, if running the command:
```shell
user@domain:~$/../aoc/python3 aoc.py 1 2025
```
The following structure is crated:
```
root/
|---2025/
    |---d_1/
        |---day_1.py
        |---input.txt
```

4. The `input.txt` will populate with that day's input specific to your login session. The `day_#.py` contains boilerplate code to read the input.

## Dependencies
If using UV, you can install the dependent packages via `uv sync`. Alternatively, a `requirements.txt` is included to run the script -- no additional packages/libraries included from the base interpreter (i.e. Python 3.12).
```pip-requirements
python-dotenv==1.2.1
requests==2.32.5
```