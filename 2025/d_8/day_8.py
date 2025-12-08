#!/usr/bin/python3
# edit the line above to the appropriate path if required

from math import sqrt
from itertools import combinations


def get_distance(a:str, b:str):
    x1, y1, z1 = a.split(",")
    x2, y2, z2 = b.split(",")

    return sqrt(((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2 + (int(z2) - int(z1))**2))


def make_circuits(edges:list[tuple[str, str]], stop:int, pt:int):
    circuits = {}
    seen = set()
    count = 0
    prev = None
    for edge in edges:
        if pt == 1 and count == stop:
            break
        elif pt == 2 and len(seen) == stop:
            break

        u, v = (edge[0], edge[1])
        if not (u in circuits.get(v, []) and v in circuits.get(u, [])):
            circuits[u] = circuits.get(u, []) + [v]
            circuits[v] = circuits.get(v, []) + [u]
            count += 1
            seen.add(u)
            seen.add(v)
            prev = (u, v)

    return circuits, prev


def get_circuit_size(box:str, circuits:dict, seen:set):
    seen.add(box)
    if box not in circuits:
        return 1
    
    else:
        edges = circuits.get(box)
        count = 1
        for e in edges:
            if e not in seen:
                count += get_circuit_size(e, circuits, seen)
                seen.add(e)
        
        return count


def solve(sorted_conns:list, stop:int, pt:int):
    circuit, prev = make_circuits(sorted_conns, stop, pt)

    if pt == 1:
        seen = set()
        count = []
        for node in coords:
            if node not in seen:
                count.append(get_circuit_size(node, circuit, seen))  
        count = sorted(count, reverse=True)
        
        return count[0] * count[1] * count[2]
    
    else:
        x1 = int(prev[0].split(",")[0])
        x2 = int(prev[1].split(",")[0])

        return x1 * x2

    
if __name__ == "__main__":
    coords = []
    with open("input.txt", "r") as file:
        for line in file:
            coords.append(line.strip())
    
    conns = {}
    for a, b in combinations(coords, 2):
        conns[(a, b)] = get_distance(a, b)
    
    sorted_conns = dict(sorted(conns.items(), key=lambda dist: dist[1]))
    print(solve(list(sorted_conns.keys()), 1000, 1))
    print(solve(list(sorted_conns.keys()), len(coords), 2))
