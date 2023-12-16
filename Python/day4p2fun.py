data = list(open("day4input.txt"))
cards = [1] * len(data)

for i, line in enumerate(data):
    winning, drawn = map(str.split, line.split("|"))

    for j in range(len(set(winning) & set(drawn))):
        cards[i + j + 1] += cards[i]

print(sum(cards))
