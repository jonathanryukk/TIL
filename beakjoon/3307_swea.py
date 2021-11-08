T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = [1] * N

    for i in range(1, N):
        maxV = 0
        for j in range(i-1, -1, -1):
            if numbers[i] >= numbers[j]:
                if maxV < dp[j]:
                    maxV = dp[j]
        dp[i] = maxV + 1

    print(f'#{tc} {max(dp)}')