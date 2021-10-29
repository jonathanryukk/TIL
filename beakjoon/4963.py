dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(x, y):
    visited[x][y] = 1
    Q = [(x, y)]
    while Q:
        x, y = Q.pop()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    print(cnt)
