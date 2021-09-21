def dfs(v):
    global cnt
    visited[v] = 1
    for i in range(1, N + 1):
        if visited[i] == 0 and G[v][i] == 1:
            cnt += 1
            dfs(i)
    return cnt


N = int(input())
M = int(input())
G = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

print(dfs(1))
