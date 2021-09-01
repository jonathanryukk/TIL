t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    result = 0
    for i in range(N):
        a, b = map(float, input().split())
        result += (a*b)

    print(f'#{tc} {result:6f}')