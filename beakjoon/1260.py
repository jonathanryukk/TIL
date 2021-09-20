def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, N + 1):
            if edge[v][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1


def dfs(v):
    visited2[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if edge[v][i] == 1 and visited2[i] == 0:
            dfs(i)


N, M, V = map(int, input().split())
edge = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
visited2 = [0] * (N + 1)


for j in range(M):
    a, b = map(int, input().split())
    edge[a][b] = 1
    edge[b][a] = 1

dfs(V)
print()
bfs(V)
