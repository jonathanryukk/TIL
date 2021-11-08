def dfs():
    global cnt
    


t = int(input())
for tc in range(1, t + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    sumV = 0
    dfs()