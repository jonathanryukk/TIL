dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    Q = [(x, y)]
    visited[x][y] = 1
    while Q:
        x, y = Q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > t and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx,ny))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

for t in range(0,max(max(arr))):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > t and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    if res < cnt:
        res = cnt

print(res)