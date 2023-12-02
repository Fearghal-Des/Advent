import os
import re
os.chdir("C:/Users/fearg/Documents/advent/two")

def read_input():
    input_file = open("./input.txt", "r")
    input_list = [line.strip() for line in input_file.readlines()]
    input_file.close()
    return input_list

def process_input(string):
    first, second = string.split(":")
    result = re.split(r',|;', second)
    min_red = 0
    min_green = 0
    min_blue = 0
    for item in result:
        # if int(item.split(" ")[1]) > max_dict[item.split(" ")[2]]:
        #     return 0
        if item.split(" ")[2] == "red" and int(item.split(" ")[1]) > min_red:
            min_red = int(item.split(" ")[1])
        elif item.split(" ")[2] == "green" and int(item.split(" ")[1]) > min_green:
            min_green = int(item.split(" ")[1])
        elif item.split(" ")[2] == "blue" and int(item.split(" ")[1]) > min_blue:
            min_blue = int(item.split(" ")[1])
            
    return min_red * min_green * min_blue


def main():
    count = 0
    input_list = read_input()
    for string in input_list:
        count += int(process_input(string))
    print(count)

if __name__ == "__main__":
    main()