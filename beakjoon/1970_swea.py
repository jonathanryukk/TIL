change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())
for tc in range(1, t + 1):
    cnt = [0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())

    for i in range(8):
        if N // change[i] != 0:
            cnt[i] = N // change[i]
            N = N % change[i]

    print(f'#{tc}')
    print(*cnt)
