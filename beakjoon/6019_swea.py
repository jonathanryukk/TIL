t = int(input())

for tc in range(1, t + 1):
    D, A, B, F = map(int, input().split())
    meetH = D/(A+B)
    print('#{} {:.6f}'.format(tc, F*meetH))

    #파리가 이동한거리 = 파리속력 * (거리/속력)

