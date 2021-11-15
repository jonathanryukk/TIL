t = int(input())


def solve(x, res):
    global min_res
    if x == n and res < min_res:
        min_res = res
        return

    if res > min_res:
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                solve(x + 1, res + arr[i][x])
                visited[i] = 0


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_res = 9999

    solve(0, 0)

    print(f'#{tc} {min_res}')
