t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N - 1):
        if (arr[i - 1] < arr[i]) and (arr[i] < arr[i + 1]):
            cnt+=1
        elif (arr[i - 1] > arr[i]) and (arr[i] > arr[i + 1]):
            cnt+=1
    print(f'#{tc} {cnt}')
