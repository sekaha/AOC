from math import ceil, floor

with open("res/day6input.txt") as file:
    time, distance = [int("".join(l.split()[1:])) for l in file]
    lowest = ceil((-time + (time**2 - 4 * distance) ** 0.5) / -2)
    highest = floor((-time - (time**2 - 4 * distance) ** 0.5) / -2)
    print(highest - lowest + 1)
