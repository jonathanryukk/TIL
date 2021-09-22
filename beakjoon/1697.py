def bfs():
    Q = [N]
    while Q:
        x = Q.pop(0)
        if x == K:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < 100001 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                Q.append(nx)


N, K = map(int, input().split())
cnt = 0
dist = [0] * 100001

bfs()
