import sys

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
Q = []
visited = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            Q.append([i, j])

def bfs():
    while Q:
        x, y = Q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                Q.append([nx, ny])
bfs()
result = 0
check = False

for i in arr:
    for j in i:
        if j == 0:
            check = True
        result = max(result,j)


if check:
    print(-1)
elif result ==-1:
    print(0)
else:
    print(result-1)
