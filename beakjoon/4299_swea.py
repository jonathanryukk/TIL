t = int(input())

for tc in range(1, t + 1):
    D, H, M = map(int, input().split())
    D1, H1, M1 = 0, 0, 0

    result = (11 * 60 * 24) + (11 * 60) + 11

    result1 = (D * 60 * 24) + (H * 60) + M

    sum1 = result1 - result

    if sum1 >= 0:
        print(f'#{tc} {sum1}')
    else:
        print(f'#{tc} -1')
