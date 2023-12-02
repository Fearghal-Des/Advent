import re
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4, 
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def read_file():
    # read in the input.txt file
    # return the input as a list of strings
    input_file = open("input-two.txt", "r")
    print("Name of the file: ", input_file.name)
    input_list = input_file.readlines()
    print("Input list: ", input_list)
    input_file.close()
    return input_list

def extract_and_convert(string):
    # Extract all digit and word representations of digits
    matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', string, re.IGNORECASE)

    # Convert extracted values to integers
    converted = []
    for match in matches:
        if match.lower() in digits_dict:
            converted.append(digits_dict[match.lower()])
        elif match.isdigit():
            converted.append(int(match))

    return converted

def calculate_calibration_value(string):
    converted_values = extract_and_convert(string)
    return converted_values[0] * 10 + converted_values[-1]

    # if converted_values:
    #     # Using the first and last values for calculation
    #     first_value = converted_values[0]
    #     last_value = converted_values[-1]
    #     return first_value * 10 + last_value
    # else:
    #     return 0
    
total_value = sum([calculate_calibration_value(string) for string in read_file()])
print(extract_and_convert("eighttwothree"))
print(extract_and_convert("eighthree"))
print(extract_and_convert("sevenine"))
print(extract_and_convert("265one"))
print(total_value)

