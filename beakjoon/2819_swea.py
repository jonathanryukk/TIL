t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(i, j, num, idx):
    if idx == 7:
        ans.add(num)
    else:
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                dfs(ni, nj, num * 10 + arr[ni][nj], idx + 1)


for tc in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    ans = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j], 1)

    print(f'#{tc} {len(ans)}')
