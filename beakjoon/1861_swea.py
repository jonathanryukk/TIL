t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, cnt):
    global result
    if cnt >= result:

    if
        result = cnt

    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[x][y] = arr[nx][ny]+1:
                dfs[nx, ny, cnt + 1]


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 999

    for i in range(n):
        for j in range(n):
            dfs(i, j, 0)
