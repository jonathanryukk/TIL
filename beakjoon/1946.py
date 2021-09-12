import sys

t = int(input())

for tc in range(t):
    N = int(input())
    arr = list([0, 0] for _ in range(N))
    cnt = 1

    for i in range(N):
        arr[i][0], arr[i][1] = map(int, sys.stdin.readline().split())

    arr.sort(key=lambda x: x[0])
    temp = arr[0][1]
    for i in range(1, N):
        if temp > arr[i][1]:
            cnt += 1
            temp = arr[i][1]

    print(cnt)
    #
    # for i in range(1,N):
    #     if temp > arr[i][1]

    # for i in range(N):
    #     mcnt = 0
    #     for j in range(N):
    #         if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
    #             mcnt += 1
    #             break
    #     if mcnt == 0:
    #         cnt += 1

