# task 1
TEST_INPUT = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()

with open("day14.txt") as f:
    TEST_INPUT = f.read().splitlines()

formatted_input = []
for line in TEST_INPUT:
    formatted_input.append([l for l in line])

for i, line in enumerate(formatted_input):
    for j, space in enumerate(line):
        replaced = False
        if space == "O":
            for k in reversed(range(0, i)):
                if formatted_input[k][j] in ["#", "O"]:
                    formatted_input[i][j] = "."
                    formatted_input[k + 1][j] = "O"
                    replaced = True
                    break
            if replaced == False:
                formatted_input[i][j] = "."
                formatted_input[0][j] = "O"

load = 0

for i in range(len(formatted_input)):
    for j in range(len(formatted_input[i])):
        if formatted_input[i][j] == "O":
            load += len(formatted_input) - i

print(load)