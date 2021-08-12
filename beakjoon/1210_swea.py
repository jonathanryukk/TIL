N, M = 100, 100

t = 10

for i in range(1,t+1):
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(M):
            if arr[j][i] == 0:
                break
            else: 
                if 0 < i < N-1: 
                    if arr[j][i+1] == 1:
                        while arr[j][i + 1] != 0:
                            i += 1
                    elif arr[j][i-1] == 1:
                        while arr[j][i-1] == 0 or i-1 != 0:
                            i -= 1
            if i == N-1:
                if i == 
                

