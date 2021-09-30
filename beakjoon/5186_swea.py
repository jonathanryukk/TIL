t = int(input())

for tc in range(1, t + 1):
    N = float(input())
    cnt = 1
    result = ''
    while N != 0:
        if N // (2 ** -cnt) >= 1:
            result += '1'
            N -= (2 ** -cnt)
        else:
            result += '0'
        cnt += 1

    if len(result) <= 12:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} overflow')
