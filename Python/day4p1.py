import re

total = 0

for line in open("day4input.txt"):
    data = re.search(r":(.*)\|(.*)", line)

    winning = set(data.group(1).split())
    drawn = set(data.group(2).split())
    matched = winning & drawn

    if len(matched) > 0:
        total += 2 ** (len(matched) - 1)

print(total)
