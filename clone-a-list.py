xs = [3, 4, 5]

print(xs.copy(), xs.copy())

print(xs[:], xs[:])

from copy import deepcopy
print(deepcopy(xs))

# [3, 4, 5]