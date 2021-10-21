t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    N1 = sorted(list(map(int,input().split())))
    M1 = list(map(int, input().split()))

    cnt = 0
    for i in M1:
        start = 0
        end = N-1

        flag = 0
        while start <= end:
            mid = (start + end) // 2

            if i >= N1[mid]:
                if i == N1[mid]:
                    cnt += 1
                    break

                start = mid + 1
                if flag == 1: break
                flag = 1

            elif i < N1[mid]:
                end = mid - 1
                if flag == -1: break
                flag = -1

    print(f'#{tc} {cnt}')