# read in the txt file from input.txt

import sys
import os

def read_input():
    # read in the input.txt file
    # return the input as a list of strings
    input_file = open("input.txt", "r")
    print("Name of the file: ", input_file.name)
    input_list = input_file.readlines()
    input_file.close()
    print("Input list: ", input_list)
    return input_list

def get_first_integer_in_string(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]
        
def get_last_integer_in_string(string):
    for i in range(1, len(string) + 1):
        if string[-i].isdigit():
            return string[-i]

def calculate_line_value(string):
    print(int(get_first_integer_in_string(string))*10 + int(get_last_integer_in_string(string)))
    return int(get_first_integer_in_string(string))*10 + int(get_last_integer_in_string(string))

def calculate_total_value(input_list):
    total_value = 0
    for string in input_list:
        total_value += calculate_line_value(string)
    return total_value

def main():
    input_list = read_input()
    total_value = calculate_total_value(input_list)
    print(total_value)

if __name__ == "__main__":
    main()