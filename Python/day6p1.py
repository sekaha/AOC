with open("res/day6input.txt") as file:
    possibilites = 1

    for time, distance in zip(*[map(int, l.split()[1:]) for l in file]):
        lowest, highest = 0, 0
        l, r = 0, time // 2

        # find lowest hold time that will win
        while l <= r:
            m = l + (r - l) // 2
            traveled = (time - m) * m

            if traveled > distance:
                lowest = m
                r = m - 1
            else:
                l = m + 1

        # find highest hold time that will win
        l, r = time // 2, time

        # find lowest hold time that will win
        while l <= r:
            m = l + (r - l) // 2
            traveled = (time - m) * m

            if traveled > distance:
                highest = m
                l = m + 1
            else:
                r = m - 1

        possibilites *= highest - lowest + 1

print(possibilites)
