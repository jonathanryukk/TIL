t = int(input())
dx = [1, -1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]


def check(x, y, color):
    arr[x][y] = color
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        Q = []
        while 0 <= nx < n  and 0 <= ny < n:
            if arr[nx][ny] == 0:
                break
            if arr[nx][ny] == color:
                for nx, ny in Q:
                    arr[nx][ny] = color
                break
            Q.append((nx, ny))
            nx, ny = nx + dx[k], ny + dy[k]


for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]
    arr[n // 2 - 1][n // 2 - 1], arr[n // 2 - 1][n // 2], arr[n // 2][n // 2 - 1], arr[n // 2][n // 2] = 2, 1, 1, 2

    for i in range(m):
        x, y, c = map(int, input().split())
        check(x-1, y-1, c)

    white = 0
    black = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
