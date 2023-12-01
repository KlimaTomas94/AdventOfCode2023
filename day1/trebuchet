#The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover.
#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#Consider your entire calibration document. What is the sum of all of the calibration values?

# Find first number in a string
def find_first_number(line):
    for char in line:
        if char.isdigit():
            return char

# Find last number in a string
def find_last_number(line):
    for char in reversed(line):
        if char.isdigit():
            return char

result = 0

# Open the file in read mode
with open('day1/trebuchet_input.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        first = find_first_number(line)
        last = find_last_number(line)
        result = result + int(first + last)

# Print result
print(result)