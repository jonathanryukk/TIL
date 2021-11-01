m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []
visited = [[0] * n for _ in range(m)]


def bfs(x, y):
    Q = [(x, y)]
    visited[x][y] = 1
    cnt = 0
    while Q:
        x, y = Q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))
        cnt += 1
    ans.append(cnt)


for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            arr[x][y] = 1
result = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j] == 0:
            result += 1
            bfs(i, j)
ans.sort()
print(result)
for i in ans:
    print(i, end=' ')
