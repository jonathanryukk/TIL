N = int(input())
arr = []
for i in range(N):
    a = list(map(int, input()))
    arr.append(a)

arrcnt = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    Q = [[i, j]]
    arr[i][j] = 0
    cnt = 1
    while Q:
        x, y = Q.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                Q.append([nx, ny])
                cnt += 1
    arrcnt.append(cnt)


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(i, j)

arrcnt.sort()
print(len(arrcnt))
for i in arrcnt:
    print(i)
