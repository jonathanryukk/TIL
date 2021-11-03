from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global result
    Q = deque()
    Q.appendleft((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.popleft()

        if arr[x][y] == '3':
            return 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100 and visited[nx][ny] == 0 and arr[nx][ny] != '1':
                visited[nx][ny] = 1
                Q.append((nx, ny))
    return 0


for ttt in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == '2':
                si, sj = i, j
                break
    visited = [[0] * 100 for _ in range(100)]

    print(f'#{tc} {bfs(si, sj)}')
