import sqlite3

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = [[] for _ in range(n)]


def bfs(s, e):
    Q = lst[s]

    while Q:
        x = Q.pop()
        if x == e:
            return 1
        for i in lst[x]:
            Q.append(i)
    return 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            lst[i].append(j)
print(lst)

newarr= [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        newarr[i][j] = bfs(i, j)

print(newarr)
