t = int(input())


def dfs(x, y, tmp):
    global res
    if 0 not in visited:
        res = min(res, tmp)
        return

    if res <= tmp:
        return

    for k in range(n):
        if visited[k] == 0:
            visited[k] = 1
            dfs(x + 1, k, tmp + arr[x + 1][k])
            visited[k] = 0


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 1000
    for i in range(n):
        visited = [0] * n
        visited[i] = 1
        dfs(0, i, arr[0][i])

    print(f'#{tc} {res}')
