T = int(input())
dx = [0, 1]
dy = [1, 0]

def dfs(s):
    global sub_cnt, cnt
    x, y = s
    if sub_cnt > cnt:
        return

    if x == N - 1 and y == N - 1:
        cnt = sub_cnt
        return

    for k in range(2):
        nx = x + dy[k]
        ny = y + dx[k]
        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1 and (nx, ny) not in visited:
            visited.append((nx, ny))
            sub_cnt += arr[nx][ny]
            dfs((nx, ny))
            visited.remove((nx, ny))
            sub_cnt -= arr[nx][ny]


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    sub_cnt, cnt = arr[0][0], 1000
    dfs((0, 0))
    print("#{} {}".format(tc, cnt))
