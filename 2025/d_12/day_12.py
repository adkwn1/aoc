#!/usr/bin/python3
# edit the line above to the appropriate path if required


SHAPES = {}
TILE_COUNT = []
RGNS = tuple()
SHAPE_W = 3
SHAPE_H = 3


def process_raw_shapes(line:str):
    idx, s = line.split(":")
    shape = []
    count = 0
    for row in s.strip().split('\n'):
        shape.append([1 if r == "#" else 0 for r in row])
        count += sum(ch == "#" for ch in row)

    shape_90 = []
    for m in range(len(shape)):
        inner = []
        for n in range(len(shape[0])-1, -1, -1):
            inner.append(shape[n][m])
        shape_90.append(inner)

    shape_180 = []
    for m in range(len(shape_90)):
        inner = []
        for n in range(len(shape_90[0])-1, -1, -1):
            inner.append(shape_90[n][m])
        shape_180.append(inner)
    
    shape_270 = []
    for m in range(len(shape_180)):
        inner = []
        for n in range(len(shape_180[0])-1, -1, -1):
            inner.append(shape_180[n][m])
        shape_270.append(inner)
    
    all_shapes = {int(idx): [shape, shape_90, shape_180, shape_270]}
        
    return all_shapes, count

    
def process_raw_regions(line:str):
    rgns = []
    for row in line.split("\n"):
        area, req = row.split(":")
        (w, h) = area.strip().split("x")
        (w, h) = (int(w), int(h))
        req = tuple(int(_) for _ in req.strip().split(" "))
        
        rgns.append(((w, h), req))

    return rgns


def place_tile(piece:list[list], area:list[list], rem:tuple[int], states={}):
    if all(i == 0 for i in rem):
        return 1

    # Memoize states
    # if unable to place
    #  return 0
    count = 0
    for idx, r in enumerate(reqs):
        if r > 0:
            count += place_tile()
    
    # Update memo

    return count


def solve(width:int, height:int, req:list[int]) -> int:
    if (width//SHAPE_W)*(height//SHAPE_H) >= sum(req):
        return 1
    
    area = width*height
    tiles_needed = sum(quantity*num_tiles for quantity, num_tiles in zip(req, TILE_COUNT))
    if area < tiles_needed:
        return 0
    
    print(req)
    return None


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        *raw_shapes, raw_regions = file.read().split("\n\n")

    for rs in raw_shapes:
        s, tc = process_raw_shapes(rs)
        SHAPES.update(s)
        TILE_COUNT.append(tc)
    
    RGNS = process_raw_regions(raw_regions)   

    total = 0
    for (width, height), reqs in RGNS:
        total += solve(width, height, reqs)
    
    print(total)
