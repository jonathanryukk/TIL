dx = [1, 0]
dy = [0, 1]


def dfs(x, y):
    global cnt,res

    if cnt > res:
        return
    if x == n - 1 and y == n - 1:
        res = cnt
        return

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += arr[nx][ny]
            dfs(nx,ny)
            cnt -= arr[nx][ny]
            visited[nx][ny] = 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = arr[0][0]
    res = 1000
    dfs(0, 0)
    print(f'#{tc} {res}')

