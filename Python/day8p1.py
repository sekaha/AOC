import re

with open("res/day8input.txt") as file:
    directions, *mappings = [line.strip() for line in file]
    directions = [d == "R" for d in directions]

    search = {
        parent: (l, r)
        for m in mappings[1:]
        if (match := re.match(r"(.*) = \((.*), (.*)\)", m))
        for parent, l, r in [match.groups()]
    }

steps, token = 0, "AAA"

while token != "ZZZ":
    i = directions[steps % len(directions)]
    token, steps = search[token][i], steps + 1

print(steps)
