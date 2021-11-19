def shoot():
    for i in range(W):
        for j in range(H):
            if arr[i][j] !=0:
                dfs()

def find(x, y):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                cnt += 1

def dfs():
    pass


t = int(input())

for tc in range(1, t + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    Q = []
    for i in range(W):
        for j in range(H):
            if
