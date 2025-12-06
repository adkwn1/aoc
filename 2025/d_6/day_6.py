#!/usr/bin/python3
# edit the line above to the appropriate path if required
                                                     
def solve(homework:list[str]) -> int:
    homework = [line.split() for line in homework]
    first = homework.pop(0)            
    ops = homework.pop(-1)
    count = 0

    for i in range(len(ops)):
        nums = int(first[i])
        for row in homework:
            if ops[i] == "*":
                nums *= int(row[i])
            else:
                nums += int(row[i])
        count += nums
    
    return count        


def solve2(homework:list[str]) -> int:
    count = key = 0
    ops = homework.pop(-1).split()
    col_nums = {i:[] for i in range(len(ops))}
    
    for col in range(len(homework[0])):
        digits = ""
        for row in homework:
            digits += row[col]
        
        if digits.strip():
            col_nums[key].append(int(digits.strip()))
        else:
            key += 1

    for k, v in col_nums.items():
        nums = v.pop(0)
        for n in v:
            if ops[k] == "*":
                nums *= n
            else:
                nums += n
        count += nums
    
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        homework = file.read().split("\n")
        
    print(solve(homework))
    print(solve2(homework))
