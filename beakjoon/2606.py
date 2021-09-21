def bfs(v):
    cnt = 0
    Q = []
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for i in range(1, N + 1):
            if G[v][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


N = int(input())
M = int(input())
G = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

print(bfs(1))
