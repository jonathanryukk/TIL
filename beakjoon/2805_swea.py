t = int(input())

for tc in range(1, t + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    sum1 = 0
    if N >= 3:
        for i in range(N // 2 + 1):
            for j in range(N // 2 + 1):
                if i + j >= N // 2:
                    sum1 += arr[i][j]

        for i in range(N // 2 + 1):
            for j in range(N // 2 + 1):
                if i >= j:
                    sum1 += arr[i][j + N // 2]

        for i in range(N // 2 + 1):
            for j in range(N // 2 + 1):
                if j >= i:
                    sum1 += arr[i + (N // 2)][j]

        for i in range(N // 2 + 1):
            for j in range(N // 2 + 1):
                if i + j <= N // 2:
                    sum1 += arr[i + (N // 2)][j + (N // 2)]

        for i in range(N):
            sum1 -= arr[N // 2][i]
            sum1 -= arr[i][N // 2]
        sum1 -= arr[N // 2][N // 2]
    else:
        sum1 = arr[0][0]
    print(f'#{tc} {sum1}')
