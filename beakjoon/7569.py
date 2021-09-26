import sys
from collections import deque

# input = sys.stdin.readline

M, N, H = map(int, input().split())

floors = []

for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append(list(map(int, input().split())))

    floors.append(floor)

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if (floors[i][j][k] == 1):
                queue.append([i, j, k])

# 이전 문제랑 다른 점은 높이가 추가됨
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

while queue:
    height, row, col = queue.popleft()

    for k in range(6):
        _height = height + dh[k]
        _row = row + dy[k]
        _col = col + dx[k]

        if 0 <= _height < H and 0 <= _row < N and 0 <= _col < M and floors[_height][_row][_col] == 0:
            queue.append([_height, _row, _col])
            floors[_height][_row][_col] = floors[height][row][col] + 1

check_tot = False
result = -2

for i in floors:
    for j in i:
        for k in j:
            if (k == 0):
                check_tot = True
            result = max(result, k)

if check_tot:
    print(-1)
elif (result == -1):
    print(0)
else:
    print(result - 1)