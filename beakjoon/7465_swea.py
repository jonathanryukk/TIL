t = int(input())


def bfs(s):
    q = [s]
    friend[s] = 1
    while q:
        new = q.pop()
        for i in range(1,n+1):
            if not friend[i] and arr[new][i]:
                friend[i] =1
                q.append(i)



for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1

    ans = 0

    friend = [0] * (n + 1)

    for i in range(1, n + 1):
        if not friend[i]:
            ans += 1
            bfs(i)

    print(f'#{tc} {ans}')