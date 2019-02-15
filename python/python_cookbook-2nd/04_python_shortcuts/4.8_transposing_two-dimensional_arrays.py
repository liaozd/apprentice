arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in map(list, zip(*arr)):
    print(i)
