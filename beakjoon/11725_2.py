import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

que = [1]
visit = [0 for i in range(n+1)]
result = {}
while que:
    now = que.pop(0)
    for i in tree[now]:
        if visit[i] == 0:
            result[i] = now
            visit[i] = 1
            que.append(i)
for i in range(2, n+1):
    print(result[i])

