neighborhood = [list(line.strip()) for line in open("res/day3input.txt")]


def get_num(x, y):
    if 0 <= y < len(neighborhood) and 0 <= x < len(neighborhood[0]):
        if neighborhood[y][x].isdigit():
            tmp = neighborhood[y][x]
            neighborhood[y][x] = "."

            return get_num(x - 1, y) + tmp + get_num(x + 1, y)
    return ""


def process_neighbors(x, y):
    part_nums = [
        int(num)
        for x_off in range(-1, 2)
        for y_off in range(-1, 2)
        if (num := get_num(x + x_off, y + y_off))
    ]

    if len(part_nums) == 2:
        return part_nums[0] * part_nums[1]

    return 0


print(
    sum(
        process_neighbors(x, y)
        for y, line in enumerate(neighborhood)
        for x, c in enumerate(line)
        if c == "*"
    )
)
