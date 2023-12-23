import os
import re
os.chdir("C:/Users/fearg/Documents/advent/3")

def read_input():
    input_file = open("./input.txt", "r")
    input_list = [line.strip() for line in input_file.readlines()]
    input_file.close()
    return input_list

def is_symbol(char):
    # return char in ["*", "#", "+", "$"]
    return not(char.isdigit() or char == ".")

def process_input(input):
    count = 0

    for i, line in enumerate(input):
        for match in re.finditer(r'\d+', line):
            num_str = match.group()
            num_start, num_end = match.start(), match.end()
            print(num_str)
            print(num_start)
            print(num_end)

            symbol_found = False
            # Check adjacent characters for each digit in the number
            for j in range(num_start, num_end):
                for x in range(max(0, i - 1), min(len(input), i + 2)):
                    for y in range(max(0, j - 1), min(len(line), j + 2)):
                        if (x != i or y != j) and is_symbol(input[x][y]):
                            symbol_found = True
                            break
                    if symbol_found:
                        break
                if symbol_found:
                    break
            
            if symbol_found:
                count += int(num_str)

    return count

def process_input_part_two(input):
    
    total = 0
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            if char == "*":
                values = set()
                
                # Iterate over the 3x3 grid centered on the '*'
                for x in range(max(0, row - 1), min(len(input), row + 2)):
                    numbers = list(re.finditer(r'\d+', input[x]))
                    for y in range(max(0, col - 1), min(len(line), col + 2)):
                        if (x != row or y != col) and input[x][y].isdigit():
                            for number in numbers:
                                if number.start() <= y <= number.end() - 1:
                                    values.add(int(number.group()))
                            
                if len(values) == 2:
                    total += prod(values)

    return total

def prod(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result



def main():
    list = read_input()
    # numbers = process_input(list)
    number = process_input_part_two(list)
    print(number)

    # print(numbers)

if __name__ == "__main__":
    main()
