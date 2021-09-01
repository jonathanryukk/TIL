t = int(input())
a = {0: 3, 1: 4, 2: 5, 3: 6, 4: 0, 5: 1, 6: 2}
b = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

for tc in range(1, t + 1):
    M, D = map(int, input().split())
    result = (b[M - 1] + D) % 7
    print(f'#{tc} {a[result]}')
