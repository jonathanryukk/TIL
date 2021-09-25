from collections import deque


def findtops(board):
    tops = []
    maxH = -1
    for r in range(N):
        for c in range(N):
            if board[r][c] == maxH:
                tops.append((r, c))
            elif board[r][c] > maxH:
                tops = [(r, c)]
                maxH = board[r][c]
    return tops


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def BFS(row, col):
    maxLevel = -1
    q = deque()
    q.append((row, col, 1, board[row][col]))
    while q:
        row, col, level, before = q.popleft()
        maxLevel = max(level, maxLevel)
        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] < before:
                q.append((nr, nc, level + 1, board[nr][nc]))
    return maxLevel


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    tops = findtops(board)

    maxLevel = -1
    for r in range(N):
        for c in range(N):
            dig = 0
            for _ in range(1, K + 1):
                board[r][c] -= 1
                dig += 1
                for top in tops:
                    if (r, c) == top:
                        continue
                    level = BFS(*top)
                    if maxLevel < level:
                        maxLevel = level
                if board[r][c] == 0:
                    break
            board[r][c] += dig

    print('#%d' % test_case, maxLevel)
