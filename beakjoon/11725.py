n = int(input())
lst = [1]
arr = [[0] * n for _ in ragne(n)]

for i in range(n):
    a, b = map(int, input().split())
    if a in lst:
        lst.append(b)
        arr[a][b] = 1
    else:
        lst.append(a)
        arr[b][a] = 1

print(arr)
