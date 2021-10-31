from itertools import permutations

n = int(input())
result = list(map(int, input().split()))
arr = list(range(1, n + 1))
lst = list(permutations(arr, n))
print(lst)
if result.pop(0) == 1:
    for i in range(n):
        print(lst[result[0] - 1][i], end=' ')
else:
    result = tuple(result)
    for i in range(len(lst)):
        if lst[i] == result:
            print(i + 1)
            break
