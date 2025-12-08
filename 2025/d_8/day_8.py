#!/usr/bin/python3
# edit the line above to the appropriate path if required

from math import sqrt
from collections import defaultdict


UNION_FIND = {}


def get_distance(a:tuple[int, int, int], b:tuple[int, int, int]) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b

    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def find(x:int):
    if x == UNION_FIND[x]:
        return x
    UNION_FIND[x] = find(UNION_FIND[x])
        
    return UNION_FIND[x]


def unite(a, b):
    UNION_FIND[find(a)] = find(b)


def solve(parents:list[tuple[int, int, int]], rels:list[tuple[float, int, int]], stop:int=1000):
    num_connections = 0

    for itx, (_d, i, j) in enumerate(rels):
        if itx == stop:
            circuit_size = defaultdict(int)
            for x in range(len(parents)):
                circuit_size[find(x)] += 1

            solution = sorted(list(circuit_size.values()))
            print(solution[-1]*solution[-2]*solution[-3])
    
        if find(i) != find(j):
            num_connections += 1
            if num_connections == (len(parents) - 1):
                print(parents[i][0] * parents[j][0])
        
        unite(i, j)


if __name__ == "__main__":
    parents = []
    with open("input.txt", "r") as file:
        for line in file.read().splitlines():
            x, y, z = [int(coord) for coord in line.split(",")]
            parents.append((x, y, z))
    
    UNION_FIND = {i: i for i in range(len(parents))}
    rels = []
    for i, a in enumerate(parents):
        for j, b in enumerate(parents):
            if i > j:
                dist = get_distance(a, b)
                rels.append((dist, i, j))

    rels = sorted(rels)
    solve(parents, rels)
