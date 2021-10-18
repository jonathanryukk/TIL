dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs1(x, y):
    Q = [(x, y)]
    visited[x][y] = 1
    while Q:
        x, y = Q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))


def bfs2(x, y):
    Q = [(x, y)]
    visited[x][y] = 1
    while Q:
        x, y = Q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))


n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * (n + 1) for _ in range(n + 1)]
cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs1(i, j)
            cnt1 += 1

visited = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs2(i, j)
            cnt2 += 1

print(cnt1, cnt2)
