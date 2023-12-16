from time import time

s = time()

# Import seed and mappings, but conver the seeds to [a,b) intervals
seeds, *mappings = open("day5input.txt").read()[:-1].split("\n\n")
seeds = [(int(s), int(sz)) for s, sz in zip(seeds.split()[1::2], seeds.split()[2::2])]
seeds = sorted([(s, s + sz) for s, sz in seeds])

for mapping in mappings:
    lookups = [list(map(int, lookup.split())) for lookup in mapping.split("\n")[1:]]
    lookups.sort(key=lambda x: x[1])
    new_seeds = []

    for (s_start, s_end) in seeds:
        for (new_start, l_start, l_length) in lookups:
            # +--------------------------------------------------------------------------------+
            # | Seed lookup interval matching cases:                                           |
            # +----------+------1------+------2------+------3------+------4------+------5------+
            # |          |   _____     |   _______   |    _____    |     _____   |   _______   |
            # | seed     |  [_****]_   |  [_*****_]  |   [*****]   |   _[****_]  |  [_______]  |
            # | lookup   |    [_____]  |   [_____]   |  [_______]  |  [_____]    |             |
            # |          |             |             |             |             |             |
            # +----------+-Terminating-+-------------+-Terminating-+-------------+-Terminating-+
            # So case 1 and 2 consider a left overhang. Case 1 the right can be flush.
            # Case 3 both can be flush. Case 4 left can be flush.
            l_end = l_start + l_length

            # Handeling the before section
            if s_start < l_start < s_end:
                new_seeds.append((s_start, l_start))
                s_start = l_start

            # Between section to be remapped
            between = (max(s_start, l_start), min(s_end, l_end))

            if between[0] < between[1]:
                offset = offset = new_start - l_start
                new_seeds.append((between[0] + offset, between[1] + offset))
                s_start = between[1]

            # early exit
            if s_end < l_start:
                break

        # Handle anything not mapped assuming it's valid (this handles the after case as well)
        if s_start < s_end:
            new_seeds.append((s_start, s_end))

        seeds = sorted(new_seeds, key=lambda x: x[0])

print(seeds[0][0])
