t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc}')

    for i in range(n):
        for x in range(n):
            print(arr[n - x - 1][i], end='')
        print(' ', end='')
        for y in range(n):
            print(arr[n - i - 1][n - y - 1], end='')
        print(' ', end='')
        for z in range(n):
            print(arr[z][n - i - 1], end='')
        print()
