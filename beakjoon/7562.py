dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]


def bfs(x1, y1, x2, y2, check):
    Q = [[x1, y1]]
    check[x1][y1] = 1
    while Q:
        x, y = Q.pop(0)
        if x == x2 and y == y2:
            print(check[x][y] - 1)
            return
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0:
                Q.append([nx, ny])
                check[nx][ny] = check[x][y] + 1

t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    check = [[0] * (N + 1) for _ in range(N + 1)]
    bfs(x1, y1, x2, y2, check)
