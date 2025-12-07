#!/usr/bin/python3
# edit the line above to the appropriate path if required


def solve1(dgram:list[list], sr:int, sc:int) -> int:
    count = 0
    moves = [(sr, sc)]
    seen = set()
    while moves:
        r, c = moves.pop(0)
        if (r, c) not in seen and dgram[r][c] == "." and r+1 < len(dgram):
            seen.add((r, c))
            moves.append((r+1, c))
        elif dgram[r][c] == "^":
            count += 1
            if (r, c-1) not in seen and c-1 < len(dgram[0]):
                moves.append((r, c-1))
            if (r, c+1) not in seen and c+1 < len(dgram[0]):
                moves.append((r, c+1))
    
    return count


def solve2(dgram:list[list], r:int, c:int, memo:dict={}) -> int:
    if (r, c) in memo:
        return memo[(r, c)]
    
    elif r >= len(dgram):
        return 1
    
    else:
        count = 0
        if dgram[r][c] == ".":
            count += solve2(dgram, r+1, c, memo)
        elif dgram[r][c] == "^": 
            count += solve2(dgram, r, c-1, memo)
            count += solve2(dgram, r, c+1, memo)
            memo[(r, c)] = count
        
        return count

                            
if __name__ == "__main__":
    diagram = []
    start = None
    with open("input.txt", "r") as file:
        for r, line in enumerate(file):
            row = []
            for c, char in enumerate(line.strip()):
                if char == "S":
                    start = (r+1, c)
                row.append(char)
            diagram.append(row)
    
    print(solve1(diagram, start[0], start[1]))
    print(solve2(diagram, start[0], start[1]))
    