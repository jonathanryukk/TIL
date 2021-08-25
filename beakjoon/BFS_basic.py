def bfs(s, V):
    q = []
    visited = [0] * (V + 1)
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)
        print(t)
        for i in range(1, V + 1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V +1)]  # 인접행렬

for i in range(E):
    n1, n2 = edge[2 * i], edge[2 * i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

bfs(1, V)
