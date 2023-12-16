import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

str_to_num = lambda s: int(numbers.get(s, s))

first_exp = "|".join(numbers.keys() | numbers.values())
last_exp = "|".join([k[::-1] for k in numbers.keys()] + list(numbers.values()))

result = 0

with open("day1input.txt") as file:
    for line in file:
        # last = re.search(last_exp, line[::-1])
        results = re.f(first_exp, line, overlapped=True)

        result += str_to_num(first.group()) * 10 + str_to_num(last.group()[::-1])

print(result)
