#!/usr/bin/python3
# edit the line above to the appropriate path if required
                            

DRX = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def check_spaces(pos:tuple[int, int], grid:list[list], num:int):
    r, c = pos
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for x, y in DRX:
        if (0 <= r+x < rows) and (0 <= c+y < cols) and grid[r+x][c+y] == "@":
            count += 1

        if count > num:
            return False
        
    return True


def remove(grid:list[list], num:int) -> tuple[int, list[tuple[int, int]]]:
    count = 0
    pos = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and check_spaces((r, c), grid, num):
                pos.append((r, c))
                count += 1

    return count, pos


def solve(grid:list[list], num:int, pt:int=1):
    count, pos = remove(grid, num)

    while pt == 2:
        for r, c in pos:
            grid[r][c] = "."
            
        new_count, pos = remove(grid, num)
        if new_count > 0:
            count += new_count
        else:
            break

    return count

                           
if __name__ == "__main__":
    grid = []
    
    with open("./input.txt", "r") as file:
        for line in file:
            grid.append([s for s in line.strip()])
    
    print(solve(grid, 3, 1), solve(grid, 3, 2))
    