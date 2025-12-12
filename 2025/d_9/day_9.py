#!/usr/bin/python3
# edit the line above to the appropriate path if required

from math import inf


def get_area(a:list[str], b:list[str]) -> int:
    w = abs(int(a[0]) - int(b[0])) + 1
    h = abs(int(a[1]) - int(b[1])) + 1
    
    return w*h


def get_line(x1, y1, x2, y2):
    return (inf, int(x1)) if not (int(x2) - int(x1)) else ((int(y2) - int(y1))/(int(x2) - int(x1)), ((int(y2) - int(y1))/(int(x2) - int(x1)))*int(x1) + int(y1))


def solve1(coords:list[str]):
    areas = {}
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i < j:
                areas[(coords[i], coords[j])] = get_area(coords[i].split(","), coords[j].split(","))
                    
    return areas


def get_segments(coords:list[str]):
    segements = {}
    for i in range(len(coords)):
        x1, y1 = coords[i-1].split(",")
        x2, y2 = coords[i].split(",")
        eq = get_line(x1, y1, x2, y2)
        segements[(coords[i], coords[i-1])] = eq
    
    return segements


def solve2(pairs:tuple[str, str], segments:dict):
    ax, ay = pairs[0].split(",")
    bx, by = pairs[1].split(",")
    a_count = 0
    b_count = 0

    min_x = min(int(ax), int(bx))
    max_x = max(int(ax), int(bx))
    min_y = min(int(ay), int(by))
    max_y = max(int(ay), int(by))
   
    for ends, eq in segments.items():
        x1, y1 = ends[0].split(",")
        x2, y2 = ends[1].split(",")
        # (0, Y) -> horizontal line through Y
        if eq[0] == 0 and (min_y < eq[1] < max_y) and not (max(int(x1), int(x2)) <= min_x or max_x <= min(int(x1), int(x2))):
            return False
        
        # (inf, X) -> vertical line through X
        elif eq[0] == inf and (min_x < eq[1] < max_x) and not (max(int(y1), int(y2)) <= min_y or max_y <= min(int(y1), int(y2))):
            return False
        
        # update ray casting count for point a
        if eq[0] == inf and (int(ax) < eq[1]) and min(int(y1), int(y2)) < int(ay) < max(int(y1), int(y2)):
            a_count += 1

        # update ray casting count for point b
        if eq[0] == inf and (int(bx) < eq[1]) and min(int(y1), int(y2)) < int(by) < max(int(y1), int(y2)):
            b_count += 1
        
    if not (a_count % 2 and b_count % 2):
        return False
    
    return True


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        coords = file.read().splitlines()
    
    rects = solve1(coords)
    print(max(rects.values()))
    
    segments = get_segments(coords)
    rects = dict(sorted(rects.items(), key=lambda pair: pair[1], reverse=True))
    for pairs, area in rects.items():
        if solve2(pairs, segments):
            print(area)
            break
        