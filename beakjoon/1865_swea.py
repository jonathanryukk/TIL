t = int(input())


def find(x, res):
    global max_res
    if x == n and res > max_res:
        max_res = res
        return

    if res <= max_res:
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                find(x + 1, res * arr[i][x] / 100)
                visited[i] = 0


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    max_res = 0
    find(0, 1)

    print('#{} {:.6f}'.format(tc, max_res * 100))
