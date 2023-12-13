# part 1


TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

with open("day9.txt") as f:
    TEST_INPUT = f.read().splitlines()

formatted_input = []
for line in TEST_INPUT:
    formatted_input.append([int(x) for x in line.split(" ")])

newest_number = 0
current_pattern = []
patterns = []
for pattern in formatted_input:
    current_pattern = []
    current_pattern.append(pattern)
    while not (all(x == 0 for x in current_pattern[-1])):
        current_pattern.append([])
        for i in range(len(current_pattern[-2]) - 1):
            current_pattern[-1].append(
                current_pattern[-2][i + 1] - current_pattern[-2][i]
            )
    patterns.append(current_pattern)

for pattern in patterns:
    for i in reversed(range(len(pattern) - 1)):
        pattern[i].append(pattern[i][-1] + pattern[i + 1][-1])
    newest_number += pattern[0][-1]

print(newest_number)
