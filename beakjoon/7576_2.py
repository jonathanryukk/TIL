from collections import deque

M, N = map(int, input().split())
tots = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if tots[i][j] == 1:
            queue.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    row, col = queue.popleft()

    for k in range(4):
        _row = row + dy[k]
        _col = col + dx[k]
        if 0 <= _row < N and 0 <= _col < M and tots[_row][_col] == 0:
            tots[_row][_col] = tots[row][col] + 1
            queue.append([_row, _col])

result = -2
check_tot = False

for i in tots:
    for j in i:
        if (j == 0):
            check_tot = True
        result = max(result, j)

if check_tot:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)