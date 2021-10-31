dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


def dfs(x, y, dot, cnt):
    global si, sj, result

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx == si and ny == sj and cnt >= 4:
            result = 1
            return
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == dot:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny, dot, cnt)
            visited[nx][ny] = 0
            cnt -= 1


for i in range(n):
    for j in range(m):
        si = i
        sj = j
        result = 0
        cnt = 0
        visited = [[0] * m for _ in range(n)]
        visited[si][sj] = 1
        dfs(si, sj, arr[si][sj], cnt)
        if result == 1:
            break
    if result == 1:
        break

if result == 1:
    print('Yes')
else:
    print('No')
