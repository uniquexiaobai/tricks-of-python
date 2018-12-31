xs = [[1, 2, 3], [4, 5, 6], [7, 8]]

flatten = lambda xs: [item for sublist in xs for item in sublist]
print(flatten(xs))

# [1, 2, 3, 4, 5, 6, 7, 8]