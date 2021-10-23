t = int(input())


def bfs(s):
    q = [s]
    team[s] = 1
    while q:
        new = q.pop()
        for i in range(1, n + 1):
            if not team[i] and arr[new][i]:
                team[i] = 1
                q.append(i)


for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # n = 출석번호(학생수) m = 신청서 장수
    arr_ = list(map(int, input().split()))
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        a, b = arr_[2*i], arr_[2*i+1]
        arr[a][b] = arr[b][a] = 1
    ans = 0

    team = [0] * (n + 1)

    for i in range(1, n + 1):
        if not team[i]:
            ans += 1
            bfs(i)

    print(f'#{tc} {ans}')
