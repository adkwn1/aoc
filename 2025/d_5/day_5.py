#!/usr/bin/python3
# edit the line above to the appropriate path if required


def solve(rngs:list[str], ids:list[int]) -> int:
    count = 0

    for i in ids:
        for rng in rngs:
            l, r = rng.split("-")
            if int(l) <= i <= int(r):
                count += 1
                break
    
    return count


def insert_rng(rngs:list[str], item:str) -> None:
    idx = len(rngs)
    for i, r in enumerate(rngs):
        if int(item[1]) < int(r[0]):
            idx = i
            break
    rngs.insert(idx, item)


def delete_indices(rngs:list[str], idx_to_del:list[int]) -> None:
    for i in sorted(idx_to_del, reverse=True):
        rngs.pop(i)


def get_overlap(rngs:list[str], idx:int, num:int, drx:int) -> str:
    new_num = num
    idx_to_del = []

    while (idx >= 0 and drx == -1) or (idx < len(rngs) and drx == 1):
        if (int(rngs[idx][0]) >= new_num and drx == -1) or (int(rngs[idx][0]) <= new_num and drx == 1):
            new_num = int(rngs[idx][0]) if drx == -1 else int(rngs[idx][1])
            idx_to_del.append(idx)
        idx += drx
    delete_indices(rngs, idx_to_del)

    return str(new_num)


def solve2(rngs:list[str]):
    count = 0
    id_rng = [r.split("-") for r in rngs]
    fresh_rng = [id_rng.pop(0)]
    while id_rng:
        curr = id_rng.pop(0)
        inserted = False
        idx_to_del = []
        for i, rng in enumerate(fresh_rng):
            # in between a current range
            if int(rng[0]) <= int(curr[0]) and int(curr[1]) <= int(rng[1]):
                inserted = True
                break
            # encompasses entire range
            elif int(curr[0]) <= int(rng[0]) and int(rng[1]) <= int(curr[1]):
                idx_to_del.append(i)
            # left in, right out
            elif int(rng[0]) <= int(curr[0]) <= int(rng[1]):
                rng[1] = get_overlap(fresh_rng, i+1, int(curr[1]), 1)
                inserted = True
                break
            # left out, right in
            elif int(rng[0]) <= int(curr[1]) <= int(rng[1]):
                rng[0] = get_overlap(fresh_rng, i-1, int(curr[0]), -1)
                inserted = True
                break
        
        delete_indices(fresh_rng, idx_to_del)
        if not inserted:
            insert_rng(fresh_rng, curr)

    for rng in fresh_rng:
        count += (int(rng[1]) - int(rng[0])) + 1

    return count


if __name__ == "__main__":    
    with open("input.txt", "r") as file:
        rngs, ids = file.read().split("\n\n")
    rngs = rngs.split("\n")
    ids = [int(i) for i in ids.split("\n")]

    print(solve(rngs, ids))
    print(solve2(rngs))
    