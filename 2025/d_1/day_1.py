#!/usr/bin/python3
# edit the line above to the appropriate path if required
                            
def solve(input:str):
    dial = 50
    count = 0

    with open(input, "r") as file:
        for line in file:
            rot = line.strip()
            dist = int(rot[1:])%100 if rot[0] == "R" else -(int(rot[1:])%100)
            new_pos = dial + dist
            if not new_pos%100:
                count += 1
            dial = new_pos%100
    
    return count


def solve2(input:str):
    dial = 50
    count = 0

    with open(input, "r") as file:
        for line in file:
            rot = line.strip()
            dist = int(rot[1:])%100 if rot[0] == "R" else -(int(rot[1:])%100)
            count += int(rot[1:])//100
            new_pos = dial + dist
            if not new_pos%100:
                count += 1
            elif dial and (new_pos<0 or new_pos>100):
                count += 1
            dial = new_pos%100
    
    return count

                            
if __name__ == "__main__":
    print(solve("./input.txt"))
    print(solve2("./input.txt"))