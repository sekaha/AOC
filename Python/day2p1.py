import re

total = 0
allowances = {"red": 12, "green": 13, "blue": 14}

with open("res/day2input.txt") as file:
    for line in file:
        header, data = line.strip().split(":")
        game_id = int(re.search(r"[0-9]+", header).group())
        rounds = data.split(";")
        valid = True

        for r in rounds:
            if not valid:
                break
            draws = r.split(",")

            for draw in draws:
                count, color = draw.strip().split(" ")

                if int(count) > allowances[color]:
                    valid = False
                    break

        if not valid:
            continue

        total += game_id
    print(total)
