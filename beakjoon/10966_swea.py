from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visited = [[-1] * m for _ in range(n)]
    _map = []
    q = deque()
    for i in range(n):
        tmp = input()
        for j in range(m):
            if tmp[j]=='W':
                q.append((i, j))
                visited[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs():
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                if visited[nx][ny] != -1: continue
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    bfs()
    result = 0
    for i in range(n):
        for j in range(m):
            result += visited[i][j]
    print("#{} {}".format(tc, result))