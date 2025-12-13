#!/usr/bin/python3
# edit the line above to the appropriate path if required

import networkx as nx


def dfs(curr, goal, E, exclude, memo):
    if curr == goal:
        return 1
    
    if memo[curr] != -1:
        return memo[curr]
    
    count = 0
    for v in E[curr]:
        if v not in exclude:
            count += dfs(v, goal, E, exclude, memo)
    memo[curr] = count

    return count


def find_all_with_passthrough(E:dict):
    num_nodes = set()
    for u, v in E.items():
        num_nodes.add(u)
        for node in v:
            num_nodes.add(node)
    
    total_paths = 1

    """
    memo = {n: -1 for n in num_nodes}
    count = dfs("dac", "fft", E, exclude, memo)
    #total_paths *= count if count != 0 else 1
    """

    exclude = ["dac", "out"]
    memo = {n: -1 for n in num_nodes}
    count = dfs("svr", "fft", E, exclude, memo)
    total_paths *= count if count != 0 else 1

    exclude = ["svr", "out"]
    memo = {n: -1 for n in num_nodes}
    count = dfs("fft", "dac", E, exclude, memo)
    total_paths *= count if count != 0 else 1

    exclude = ["svr", "fft"]
    memo = {n: -1 for n in num_nodes}
    count = dfs("dac", "out", E, exclude, memo)
    total_paths *= count if count != 0 else 1

    """
    memo = {n: -1 for n in num_nodes}
    exclude = ["fft", "out"]
    count = dfs("svr", "dac", E, exclude, memo)
    #total_paths *= count if count != 0 else 1
    """
    """
    exclude = ["svr", "dac"]
    memo = {n: -1 for n in num_nodes}
    count = dfs("fft", "out", E, exclude, memo)
    #total_paths *= count if count != 0 else 1
    """
    
    return total_paths

    
if __name__ == "__main__":
    edge_list = {}
    with open("input.txt", "r") as file:
        for line in file:
            row = line.strip().split(" ")
            edge_list[row.pop(0)[:-1]] = row
    
    G = nx.DiGraph(edge_list)

    print(len(list(nx.all_simple_paths(G, "you", "out"))))
    print(find_all_with_passthrough(edge_list))
