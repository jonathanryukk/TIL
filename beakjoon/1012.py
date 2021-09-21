T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    Q = [[i, j]]
    arr[i][j] = 0
    while Q:
        x, y = Q.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                Q.append([nx, ny])


for tc in range(1, T + 1):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    for i in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1

    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
