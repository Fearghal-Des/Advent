import os
import re
os.chdir("C:/Users/fearg/Documents/advent/4")

def read_input():
    input_file = open("./input.txt", "r")
    input_list = [line.strip() for line in input_file.readlines()]
    input_file.close()
    return input_list

def process_input(input):
    total = 0
    for line in input:
        numbers =line.split(": ")
        first_numbers = numbers[1].split(" | ")[0].split()
        second_numbers = numbers[1].split(" | ")[1].split()
        total_number = len(first_numbers) + len(second_numbers)
        set_numbers = set()
        for number in first_numbers:
            set_numbers.add(number)
        for number in second_numbers:
            set_numbers.add(number)
        add_value = 2**(total_number - len(set_numbers) - 1)
        if add_value >= 1:
            total += add_value
    return total

def process_input_two(input):
    multiplier_list = [1] * len(input)
    for line in input:
        numbers =line.split(": ")
        first_numbers = numbers[1].split(" | ")[0].split()
        second_numbers = numbers[1].split(" | ")[1].split()
        total_number = len(first_numbers) + len(second_numbers)
        set_numbers = set()
        for number in first_numbers:
            set_numbers.add(number)
        for number in second_numbers:
            set_numbers.add(number)
        for i in range(total_number - len(set_numbers)):
            if input.index(line) + i + 1 < len(input):
                multiplier_list[input.index(line) + i + 1] += multiplier_list[input.index(line)]
    return sum(multiplier_list)

print(process_input_two(read_input()))
