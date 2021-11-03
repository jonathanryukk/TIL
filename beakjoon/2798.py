from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = list(set(combinations(arr, 3)))
res = 0

for i in range(len(result)):
    if sum(result[i]) <= m and res < sum(result[i]):
        res = sum(result[i])


print(res)