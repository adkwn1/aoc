#!/usr/bin/python3
# edit the line above to the appropriate path if required


def solve1(input:str):
    count = 0
    with open(input, "r") as file:
        for line in file:
            bank = line.strip()
            first = bank[0]
            second = "0"
            for i in range(1, len(bank)):
                if int(bank[i]) > int(first) and (i < len(bank)-1):
                    first = bank[i]
                    second = bank[i+1]
                elif int(bank[i]) >= int(second):
                    second = bank[i]                    
            count += int(first + second)
    return count


def solve2(input:str):
    count = 0
    with open(input, "r") as file:
        for line in file:
            bank = line.strip()
            min_num = 100
            min_idx = 0
            array = [int(b) for b in bank[:12]]
    
            for idx, n in enumerate(array):
                if n < min_num:
                    min_num = n
                    min_idx = idx
    
            for i in range(12, len(bank)):
                if array[0] < array[1]:
                    array.pop(0)
                elif int(bank[i]) >= min_num:
                    array.pop(min_idx)
                array.append(int(bank[i]))
                min_num = min(array)
                min_idx = array.index(min_num)
            #print(array)
            count += int("".join([str(s) for s in array]))            
    
    return count

                            
if __name__ == "__main__":
    print(solve1("./input.txt"), solve2("./input.txt"))
   # print(solve2("./test.txt"))

# 150751623305028 too low
# 155590471707149 too low
# 783426553274286915064646097389328607328213 too high