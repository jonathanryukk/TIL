def dfs(i, cnt):
    global res

    if res < cnt:
        res = cnt

    for k in G[i]:
        if not v[k]:
            v[k] = 1
            dfs(k, cnt + 1)
            v[k] = 0


t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    v = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    res = 0

    for i in range(1, N + 1):
        v[i] = 1
        dfs(i, 1)
        v[i] = 0

    print(f'#{tc} {res}')
