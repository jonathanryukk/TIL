def solve(i, j):
    if j == 0:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    for k in range(n):
        if j & 1 << k:
            dp[i][j] += solve(i + arr[k], j ^ 1 << k)
            if i >= arr[k]: dp[i][j] += solve(i - arr[k], j ^ 1 << k)
    return dp[i][j]


for T in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    dp = [[-1] * (2 ** n) for i in range(sum(arr) + 1)]
    print(dp)
    print("#%d %d" % (T, solve(0, (2 ** n) - 1)))