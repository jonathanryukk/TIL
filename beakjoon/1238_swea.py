from collections import deque


def bfs(s):
    Q = deque()
    Q.append(s)
    while Q:
        mav = 0
        s = Q.pop()
        visited[s] = 1
        if mav < s:
            mav = s
        while lst[s]:
            tmp = lst[s].pop()
            if visited[tmp] ==0:
                Q.append(tmp)

    return mav


for tc in range(1, 11):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print(arr)
    lst = [[] for _ in range(100)]
    for k in range(n // 2):
        a, b = arr[2 * k], [2 * k + 1]
        if b not in lst[a]:
            lst[a].append(b)
    visited = [0] * 101

    print(f'#{tc} {bfs(s)}')
