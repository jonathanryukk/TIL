t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    suf = list(input().split())
    result = ''

    mid = (N+1) // 2

    if N % 2 == 0:
        for i in range(mid):
            result += ' ' + str(suf[i])
            result += ' ' + str(suf[i + mid])
    else:
        for i in range(mid-1):
            result += ' ' + str(suf[i])
            result += ' ' + str(suf[i + mid])
        result += ' ' + str(suf[mid-1])
    print(f'#{tc}{result}')
