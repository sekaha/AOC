arr = [[(x, y) for x in range(10)] for y in range(10)]

for v in iter(arr):
    print(next(iter(v)))
