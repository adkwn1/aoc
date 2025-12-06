#!/usr/bin/python3
# edit the line above to the appropriate path if required


def first_largest_idx(array:list):
    max_num = 0
    idx = 0

    for i, n in enumerate(array):
        if int(n) > max_num:
            max_num = int(n)
            idx = i

    return idx


def solve(input:str, size:int):
    count = 0
    with open(input, "r") as file:
        for line in file:
            bank = line.strip()
            result = []
            idx = first_largest_idx(bank)

            while len(result) < size:
                if len(bank[idx:]) >= (size - len(result)):
                    result.append(bank[idx])
                    bank = bank[idx+1:]
                    idx = first_largest_idx(bank)
                else:
                    idx = first_largest_idx(bank[:idx])
            
            count += int("".join(result))
    
    return count

                            
if __name__ == "__main__":
   print(solve("./input.txt", 2), solve("./input.txt", 12))
