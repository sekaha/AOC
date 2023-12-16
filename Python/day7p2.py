# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
hand_order = "J23456789TQKA"

# use the letter ordering as a base basically
def get_hand_val(card):
    n = 0

    for c in card:
        n *= len(hand_order)
        n += hand_order.index(c)

    return n


types = [[] for _ in range(7)]
type_order = [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [5, 0]]

with open("res/day7input.txt") as file:
    for hand, bid in (line.split() for line in file):
        counts = sorted([hand.count(c) for c in hand_order[1:]], reverse=True)[:2]
        counts[0] += hand.count("J")
        types[type_order.index(counts)].append((hand, bid))

types = sum([sorted(t, key=lambda x: get_hand_val(x[0])) for t in types], [])
total = sum((i + 1) * int(bid) for i, (hand, bid) in enumerate(types))

print(total)
