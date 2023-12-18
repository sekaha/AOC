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

    tokens = [parent for parent in search if parent.endswith("A")]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 1

for token in tokens:
    steps = 0

    while not token.endswith("Z"):
        i = directions[steps % len(directions)]
        token = search[token][i]
        steps += 1

    ans = lcm(ans, steps)

print(ans)
