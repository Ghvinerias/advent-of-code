import re

calibration_value = 0

#with open('input.txt', 'r') as file:
with open('example_input1.txt', 'r') as file:
    text = file.read()

split_text = text.split('\n')
for line in split_text:
    numbers = re.findall(r'\d', line)
    print(numbers)
    if len(numbers) == 0:
        continue
    elif len(numbers) == 1:
        numbers = [numbers[0] * 2]
    else:
        numbers = [numbers[0] + numbers[-1]]
    numbers = list(map(int, numbers))
    print(numbers)
    calibration_value += sum(numbers)

print(calibration_value)
