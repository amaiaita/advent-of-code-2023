import re

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

TEST_INPUT = TEST_INPUT.split("\n")

with open("day2.txt") as f:
    data = f.read().split("\n")

max_color_values = {"red": 12, "green": 13, "blue": 14}


def day2task1(data):
    valid_games = []
    for i, line in enumerate(data):
        data[i] = line[line.find(":") + 2 :].split(";")

    for i, game in enumerate(data):
        valid_round = 0
        for game_round in game:
            red = game_round.find("red")
            blue = game_round.find("blue")
            green = game_round.find("green")

            if red != -1:
                if int(re.findall(r"(\d+)\s+red", game_round)[0]) > 12:
                    valid_round += 1
            if green != -1:
                if int(re.findall(r"(\d+)\s+green", game_round)[0]) > 13:
                    valid_round += 1
            if blue != -1:
                if int(re.findall(r"(\d+)\s+blue", game_round)[0]) > 14:
                    valid_round += 1
        if valid_round == 0:
            valid_games.append(i + 1)

    return sum(valid_games)


def day2task2(data):
    total_power = 0

    for i, line in enumerate(data):
        data[i] = line[line.find(":") + 2 :].split(";")

    for i, game in enumerate(data):
        max_color_values = {"red": 0, "green": 0, "blue": 0}

        for game_round in game:
            red = game_round.find("red")
            blue = game_round.find("blue")
            green = game_round.find("green")

            if red != -1:
                num_red = int(re.findall(r"(\d+)\s+red", game_round)[0])
                if num_red > max_color_values["red"]:
                    max_color_values["red"] = num_red
            if green != -1:
                num_green = int(re.findall(r"(\d+)\s+green", game_round)[0])
                if num_green > max_color_values["green"]:
                    max_color_values["green"] = num_green
            if blue != -1:
                num_blue = int(re.findall(r"(\d+)\s+blue", game_round)[0])
                if num_blue > max_color_values["blue"]:
                    max_color_values["blue"] = num_blue

        total_power += (
            max_color_values["red"]
            * max_color_values["green"]
            * max_color_values["blue"]
        )

    return total_power


print(day2task2(data))
