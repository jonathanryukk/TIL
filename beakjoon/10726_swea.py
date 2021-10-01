t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().split())
    result = 'ON'

    for i in range(N):
        if M % 2 == 0:
            result = 'OFF'
            break
        else:
            M = M//2

    print(f'#{tc} {result}')
