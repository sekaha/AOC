neighborhood = [list(line.strip()) for line in open("day3input.txt")]


def get_num(x, y):
    if 0 <= y < len(neighborhood) and 0 <= x < len(neighborhood[0]):
        if neighborhood[y][x].isdigit():
            tmp = neighborhood[y][x]
            neighborhood[y][x] = "."

            return get_num(x - 1, y) + tmp + get_num(x + 1, y)
    return ""


def process_neighbors(x, y):
    sub_total = 0

    for x_off in range(-1, 2):
        for y_off in range(-1, 2):
            num = get_num(x + x_off, y + y_off)

            if num:
                sub_total += int(num)

    return sub_total


total = 0

for y, line in enumerate(neighborhood):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            total += process_neighbors(x, y)

print(total)
