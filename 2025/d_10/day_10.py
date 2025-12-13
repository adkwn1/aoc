#!/usr/bin/python3
# edit the line above to the appropriate path if required


from ast import literal_eval
from itertools import combinations
from functools import cache
from math import inf


def toggle_disp(state:str, btn:int|tuple):
    new_state = list(state)
    if isinstance(btn, int):
        new_state[btn] = "." if new_state[btn] == "#" else "#"
    
    else:
        for b in btn:
            new_state[b] = "." if new_state[b] == "#" else "#"

    return "".join(new_state)


def press_btn(state:str, buttons:list[int|tuple]) -> int:
    moves = [(state, None, 0)]
    seen = {state: 0}
    min_count = inf
    while moves:
        curr_state, skip, depth = moves.pop(0)
        
        if "#" not in curr_state and depth < min_count:
            min_count = depth
        
        for i, btn in enumerate(buttons):
            if i != skip:
                next_state = toggle_disp(curr_state, btn)
                if next_state not in seen or depth+1 < seen[next_state]:
                    moves.append((next_state, i, depth+1))
                    seen[next_state] = depth+1
    
    return min_count


# Part 2 uses solution from redditor tenthmascot
## https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/


def get_sequence(buttons:list[int|tuple]):
    res = {}
    num_btns = len(buttons)
    num_vars = len(buttons[0])
    for pattern_len in range(num_btns+1):
        for combs in combinations(range(num_btns), pattern_len):
            pattern = tuple(map(sum, zip((0,) * num_vars, *(buttons[i] for i in combs))))
            if pattern not in res:
                res[pattern] = pattern_len
                    
    return res


def press_counter(state:tuple[int], buttons:list[int|tuple]) -> int:
    costs = get_sequence(buttons)
    @cache
    def rec_solve(state:tuple[int]) -> int:
        if all(i == 0 for i in state): 
            return 0
        answer = 1_000_000
        for seq, seq_cost in costs.items():
            if all(i <= j and i % 2 == j % 2 for i, j in zip(seq, state)):
                new_goal = tuple((j - i)//2 for i, j in zip(seq, state))
                answer = min(answer, seq_cost + 2 * rec_solve(new_goal))
            
        return answer

    return rec_solve(state)


def solve(row:str):
    params = row.split(" ")
    disp = params[0][1:-1]
    buttons = [literal_eval(o) for o in params[1:-1]]
    jolts = tuple(int(j) for j in params[-1][1:-1].split(","))
    enc_btns = [[int(i) for i in r[1:-1].split(",")] for r in params[1:-1]]
    enc_btns = [tuple(int(i in r) for i in range(len(jolts))) for r in enc_btns]
    
    c1 = press_btn(disp, buttons)
    c2 = press_counter(jolts, enc_btns)
    
    return c1, c2

                           
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        rows = file.read().splitlines()
    
    total_1 = total_2 = 0
    for r in rows:
        t1, t2 = solve(r)
        total_1 += t1
        total_2 += t2

    print(total_1, total_2)
