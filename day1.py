import re

test_input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

test_input = test_input.split('\n')

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
    data = f.read().split('\n')

def day1task2(data):
    no_numbers = []

    for line in data:
        no_numbers.append(re.findall("(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))",line))

    total = 0

    for line in no_numbers:
        number = ''
        index_we_want = [0,-1]
        
        for i in index_we_want:
            if line[i].isdigit():
                number+=line[i]
            else:
                number+=str(numbers[line[i]])
        
        total+=int(number)
    
    return total

print(day1task2(test_input))
print(day1task2(data))