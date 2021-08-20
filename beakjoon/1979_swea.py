t = int(input())

for num in range(1, t + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(N - 2):
            if arr[i][j] == 1 and arr[i][j + 1] == 1 and arr[i][j + 2] == 1:
                sum(arr[i]) == 3
                cnt += 1
    for i in range(N):
        for j in range(N):
            if i > j:
                arr[i][j] = a[j][i]
    for i in range(N):
        for j in range(N - 2):
            if arr[i][j] == 1 and arr[i][j + 1] == 1 and arr[i][j + 2] == 1:
                sum(arr[i]) == 3
                cnt += 1

    print(f'#{num} {cnt}')
