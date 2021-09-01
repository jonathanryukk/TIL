t = int(input())

for tc in range(1, t + 1):
    N, P, T = map(int, input().split())

    if P > T:
        result1 = T
        if (P + T) > N:
            result2 = P + T - N
        else:
            result2 = 0
    else:
        result1 = P
        if (P + T) > N:
            result2 = P + T - N
        else:
            result2 = 0

    print(f'#{tc} {result1} {result2}')
