t = int(input())

for tc in range(1, t + 1):
    a = list(input())
    lena = len(a) // 2
    res = 'Exist'


    for i in range(lena):
        if a[i] != a[len(a) - i - 1]:
            if a[i] == '?' or a[len(a) - i - 1] == '?':
                continue
            else:
                res = 'Not exist'
                break
    print(f'#{tc} {res}')
