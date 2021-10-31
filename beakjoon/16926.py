n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
newarr = [[0] * m for _ in range(n)]

for i in range(r):
    for x in range(min(n, m) // 2):

        for y in range(i)