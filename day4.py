import re

TEST_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

with open("day4.txt") as f:
    data = f.read()


def day4task1(data):
    pattern = re.compile(r"^Card \d+: (.*)$", re.MULTILINE)
    data = pattern.sub(r"\1", data)
    data = re.sub(' +',' ', data).splitlines()
    points = 0

    for i,line in enumerate(data):
        data[i] = line.split('|')

    for i, line in enumerate(data):
        for j, half in enumerate(line):
            data[i][j] = half.strip().split(' ')

    for line in data:
        overlap = len(set(line[0])&set(line[1]))
        if overlap>0:
            points+=2**(overlap-1)
    return points

def day4task2(data):
    pattern = re.compile(r"^Card \d+: (.*)$", re.MULTILINE)
    data = pattern.sub(r"\1", data)
    data = re.sub(' +',' ', data).splitlines()

    for i,line in enumerate(data):
        data[i] = line.split('|')

    for i, line in enumerate(data):
        for j, half in enumerate(line):
            data[i][j] = half.strip().split(' ')

    number_of_cards = {}

    for i,line in enumerate(data):
        number_of_cards[i+1] = 1

    for key,value in number_of_cards.items():
        for k in range(value):
            overlap = len(set(data[key-1][0])&set(data[key-1][1]))
            for j in range(overlap):
                number_of_cards[key+j+1]+=1

    return sum(number_of_cards.values())

print(day4task2(data))
