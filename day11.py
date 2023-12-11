import numpy as np

TEST_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

with open("day11.txt") as f:
    input = f.read().splitlines()


fulL_input = []
for row in input:
    fulL_input.append([*row])


def add_expansion(list_of_lists):
    added_rows = []
    for row in list_of_lists:
        if all(x == "." for x in row):
            added_rows.append(row)
        added_rows.append(row)
    return added_rows


added_rows = add_expansion(fulL_input)

flipped = np.array(added_rows).T.tolist()

added_columns = add_expansion(flipped)
added_columns = np.array(added_columns).T.tolist()


galaxies = []
for row_number, row in enumerate(added_columns):
    for column_number, point in enumerate(row):
        if point == "#":
            galaxies.append((row_number, column_number))

total = 0
for i, galaxy in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        total += abs(galaxy[0] - galaxies[j][0]) + abs(galaxy[1] - galaxies[j][1])


print(total)
