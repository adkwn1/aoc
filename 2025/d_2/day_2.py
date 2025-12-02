#!/usr/bin/python3
# edit the line above to the appropriate path if required
                            
def solve1(input:str):
    with open(input, "r") as file:
        input = file.readline()
        count = 0
        for rng in input.split(","):
            a, b = rng.split("-")            
            for i in range(int(a), int(b)+1):
                num = str(i)
                if not len(num)%2:
                    mid = len(num)//2
                    count = count + i if num[:mid] == num[mid:] else count + 0

        return count
    
                           
def solve2(input:str):
    with open(input, "r") as file:
        input = file.readline()
        count = 0
        for rng in input.split(","):
            a, b = rng.split("-")            
            for i in range(int(a), int(b)+1):
                num = str(i)
                mid = len(num)//2
                j = 1
                while j < mid+1:
                    sub = num[:j]
                    if not len(num)%len(sub):
                        pattern = True
                        width = len(sub)
                        for k in range(0, len(num), width):
                            if num[k:k+width] != sub:
                                pattern = False
                                break
                        if pattern:
                            count = count + i
                            break
                    j += 1

        return count


if __name__ == "__main__":
    print(solve1("./input.txt"), solve2("./input.txt"))
    