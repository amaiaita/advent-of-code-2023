import re

test_input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

numbers = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

with open("day1.txt") as f:
    data = f.read()

split_test = data.split('\n')

no_numbers = []

for line in split_test:
    no_numbers.append(re.findall("(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))",line))

total = 0

for line in no_numbers:
    number = ''
    pattern = "[1-9]"
    if bool(re.search(pattern, line[0]))==False:
        number+=str(numbers[line[0]])
    else:
        number+=line[0]

    if bool(re.search(pattern, line[-1]))==False:
        number+=str(numbers[line[-1]])
    else:
        number+=line[-1]
    
    total+=int(number)

print(total)