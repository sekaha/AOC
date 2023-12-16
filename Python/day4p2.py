import re

total = 0
scratch_cards = []

for line in open("res/day4input.txt"):
    data = re.search(r":(.*)\|(.*)", line)

    winning = set(data.group(1).split())
    drawn = set(data.group(2).split())
    matches = len(winning & drawn)

    # matches on card, number of copies of this card
    scratch_cards.append([matches, 1])

for i, card in enumerate(scratch_cards):
    matches = card[0]
    copies = card[1]
    total += copies

    for j in range(matches):
        scratch_cards[i + 1 + j][1] += copies

print(total)
