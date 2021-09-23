t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        G[a][b] = 1
        G[b][a] = 1


