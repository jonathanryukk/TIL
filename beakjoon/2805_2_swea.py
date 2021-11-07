t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    sumv = 0
    cnt = 0
    x = 0
    t = n // 2
    if n == 1:
        print(f'#{tc} {arr[0][0]}')
    else:
        while x != n:
            if x < t:
                for i in range(t - cnt, t + cnt + 1):
                    sumv += arr[x][i]
                cnt += 1
            else:
                for i in range(t - cnt, t + cnt + 1):
                    sumv += arr[x][i]
                cnt -= 1
            x += 1

        print(f'#{tc} {sumv}')
