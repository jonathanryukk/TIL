for num in range(1,11):
    N = 100
    M = 100
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_max = 0

    for i in range(M):
        sum1 = 0
        for j in range(N):
            sum1 += arr[i][j]
        if sum1 > sum_max:
            sum_max = sum1

    for j in range(M):
        sum1 = 0
        for i in range(N):
            sum1 += arr[i][j]
        if sum1 > sum_max:
            sum_max = sum1

    for i in range(M):
        sum1 = 0
        sum1 += arr[i][i]

        if sum1 > sum_max:
            sum_max = sum1

    for i in range(M):
        sum1 = 0
        sum1 += arr[i][M-i-1]

        if sum1 > sum_max:
            sum_max = sum1

    print(f'#{num} {sum_max}')