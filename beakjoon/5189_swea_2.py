t = int(input())


def dfs(x, cur_minv):
    global minv

    if minv > cur_minv:
        if 0 not in visited:
            minv = min(minv, arr[x][0] + cur_minv)
            return
        for k in range(1, n):
            if visited[k] == 0 and arr[x][k] != 0:
                visited[k] = 1
                dfs(k, cur_minv + arr[x][k])
                visited[k] = 0


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minv = 1000

    for i in range(n):
        visited = [0] * n
        visited[i] = 1
        dfs(i, arr[0][i])

    dfs(0, 0)

    print(f'#{tc} {minv}')