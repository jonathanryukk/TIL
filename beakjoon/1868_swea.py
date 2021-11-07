from collections import deque

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def find(x, y):
    global cnt
    Q = deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        tmp = 0
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == '*':
                    tmp += 1
                    break
        if tmp == 0:
            if arr[x][y] != '.':

            arr[x][y] = 1
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    arr[nx][ny] = 1
                    Q.append((nx, ny))
    if tmp != 0:
        cnt += 1


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.' and not visited[i][j]:
                find(i, j)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.':
                cnt += 1

    print(f'#{tc} {cnt}')
