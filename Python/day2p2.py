from functools import reduce

total = 0

with open("day2input.txt") as file:
    for game in file:
        header, data = game.strip().split(":")
        rounds = data.split(";")
        mins = {"red": 0, "green": 0, "blue": 0}

        for r in rounds:
            draws = r.split(",")

            for draw in draws:
                count, color = draw.strip().split(" ")
                mins[color] = max(int(count), mins[color])

        total += reduce((lambda a, b: a * b), mins.values())
    print(total)
