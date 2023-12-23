import os
import re
os.chdir("C:/Users/fearg/Documents/advent/5")

def read_input():
    input_file = open("./example.txt", "r")
    input_list = [line.strip() for line in input_file.readlines()]
    input_file.close()
    return input_list

# I'm fairly happy with this map function
def map(first, second, final, value):
    if second <=  value <= second + final - 1:
        value = value - second + first 
    return value

def process_input(input_list):
    seeds = input_list[0].split("seeds: ")[1].split()
    truth_list = [False] * len(seeds)
    for line in input_list:
        if re.search(r"seeds", line):
            continue
        elif re.search(r"map", line):
            truth_list = [False] * len(seeds)
            print(line)
            continue
        elif line.strip() == "":
            continue
        else:
            map_list = line.split()
            first = int(map_list[0])
            second = int(map_list[1])
            final = int(map_list[2])
            for i in range(len(seeds)):
                if truth_list[i] == True:
                    pass
                else:
                    tmp = seeds[i]
                    seeds[i] = map(first, second, final, int(seeds[i]))
                    # print(seeds[i])
                    if seeds[i] != tmp:
                        
                        truth_list[i] = True
    return min(seeds)


            
lines = read_input()
print(process_input(lines))