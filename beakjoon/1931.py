N = int(input())
arr = [[0] * 2 for _ in range(N)]

for i in range(N):
    arr[i][0], arr[i][1] = map(int, input().split())

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
ep = arr[0][1]

for i in range(1, N):
    if arr[i][0] >= ep:
        cnt += 1
        ep = arr[i][1]

print(cnt)
