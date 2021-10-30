from itertools import permutations

n = int(input())
a = list(range(1, n + 1))
a = list(map(str, a))
arr = list(permutations(a, n))

for i in arr:
    print(' '.join(i))