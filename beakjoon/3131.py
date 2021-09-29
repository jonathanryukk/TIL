N = 1000001
arr = [1] * N
arr[0], arr[1] = 0, 0

for i in range(2, N):
    if arr[i] == 1:
        for j in range(i * 2, N, i):
            arr[j] = 0

for i in range(N):
    if arr[i] == 1:
        print(i, end=' ')
