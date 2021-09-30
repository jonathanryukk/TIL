t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]) or (arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]):
                cnt += 1

    print(f'#{tc} {cnt//2}')
