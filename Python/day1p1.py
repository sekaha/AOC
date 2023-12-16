import re

with open("day1input.txt") as lines:
    result = sum(
        int(digits[0]) * 10 + int(digits[-1])
        for line in lines
        if (digits := re.findall(r"\d", line))
    )

print(result)
