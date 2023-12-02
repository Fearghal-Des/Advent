import os
import re
os.chdir("C:/Users/fearg/Documents/advent/two")

max_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def read_input():
    input_file = open("./input.txt", "r")
    input_list = [line.strip() for line in input_file.readlines()]
    input_file.close()
    return input_list

def process_input(string):
    first, second = string.split(":")
    result = re.split(r',|;', second)
    for item in result:
        if int(item.split(" ")[1]) > max_dict[item.split(" ")[2]]:
            return 0
            
    return first.split(" ")[1]


def main():
    count = 0
    input_list = read_input()
    for string in input_list:
        count += int(process_input(string))
    print(count)

if __name__ == "__main__":
    main()