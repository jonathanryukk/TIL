# 2중 반복문 + 함수
n, m = map(int, input().split())
chess_W = [[0] * m for _ in range(n)]
chess_B = [[0] * m for _ in range(n)]
arr = [list(input()) for _ in range(n)]
cnt = float('inf')


def check(a, b):
    global cnt
    temp_W, temp_B = 0, 0
    for x in range(8):
        for y in range(8):
            if arr[a + x][b + y] != chess_W[a + x][b + y]:
                temp_W += 1
            if arr[a + x][b + y] != chess_B[a + x][b + y]:
                temp_B += 1
    cnt = min(cnt, temp_W)
    cnt = min(cnt, temp_B)
    return cnt


for i in range(n):
    for j in range(m):
        if not (i + j) % 2:
            chess_W[i][j] = 'W'
            chess_B[i][j] = 'B'
        else:
            chess_W[i][j] = 'B'
            chess_B[i][j] = 'W'

for i in range(n - 7):
    for j in range(m - 7):
        check(i, j)

print(cnt)