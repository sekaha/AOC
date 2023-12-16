# so find which range a thing belongs to.....
# then convert it, based on the offset
# if there is no range it belongs to, then the source and destination are the same number
seeds, *mappings = open("res/day5input.txt").read().split("\n\n")
seeds = list(map(int, seeds.split()[1:]))

for mapping in mappings:
    for i, seed in enumerate(seeds):
        for lookup in mapping.split("\n")[1:]:
            if lookup:  # for handling trailing \n in the input :/
                dst, src, length = map(int, lookup.split())

                if src <= seed < src + length:
                    seeds[i] = dst + (seed - src)
                    break

print(min(seeds))
