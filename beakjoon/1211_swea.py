t = 10
dx = [0, 0, 1]
dy = [-1, 1, 0] # < > v


def find(i, j, startj):
    global cnt, result, cntmin
    while True:
        for k in range(3):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                i, j = ni, nj
                cnt += 1
                break
        if i == 99:
            if cntmin >= cnt:
                cntmin = cnt
                result = startj
            break

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cntmin = 99999
    for s in range(100):
        if arr[0][s] == 1:
            visited = [[0] * 101 for _ in range(101)]
            cnt = 0
            startj = 0
            find(0, s, s)
    print(f'#{tc} {result}')