numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

input_your_phone_num = input("Enter your phone number: ")
output_str_number = ''

for i in input_your_phone_num:
    if i in numbers:  # Check if the character is a valid number
        output_str_number += numbers[i] + ' '

print(output_str_number.strip())  # Remove any trailing whitespace







