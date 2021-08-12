t = int(input())

for num in range(1,t+1):
    N,K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(N-2):
            if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1:
                if j == 0:
                    if arr[i][j+3] == 0:
                        cnt += 1
                elif j == N-3:
                    if arr[i][j-1] == 0:
                        cnt += 1
                elif arr[i][j-1] == 0 and arr[i][j+3] == 0:
                    cnt += 1
                else:
                    pass

    for i in range(N-2):
        for j in range(N):
            if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+2][j] ==1:
                if i == 0:
                    if arr[i+3][j] == 0:
                        cnt += 1
                elif i == N-3:
                    if arr[i-1][j] == 0:
                        cnt += 1
                elif arr[i-1][j] == 0 and arr[i+3][j] == 0:
                    cnt += 1
                else:
                    pass

    print(f'#{num} {cnt}')
