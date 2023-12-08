import re

# Create a dictionary to map spelled out numbers to their numeric values
number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

calibration_value = 0

with open('example_input2.txt', 'r') as file:
#with open('example_input2.txt', 'r') as file:
    text = file.read()

split_text = text.split('\n')

result = ''  # Variable to store the modified lines

for line in split_text:
    # Replace the spelled out numbers with their numeric values
    for word, number in number_dict.items():
        line = line.replace(word, number)
    
    result += line + '\n'  # Append the modified line to the result variable
    with open('new.txt', 'w') as file1:
        file1.write(result)

    
print(result)