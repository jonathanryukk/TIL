import sys

n = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [0 for i in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i + 1])

print(dp[0])
