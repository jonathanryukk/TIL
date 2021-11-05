t = int(input())

for tc in range(1, t + 1):
    n, a, b = map(int, input().split())

    temp = 'z'
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j > n:
                break
            res = (a * abs(i - j)) + (b * (n - i * j))

            if temp == 'z':
                temp = res

            if res < temp:
                temp = res

    print(f'#{tc} {temp}')
