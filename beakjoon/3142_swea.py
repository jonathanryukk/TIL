t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().split())

    x = N - M
    y = M - x

    print(f'#{tc} {y} {x}')