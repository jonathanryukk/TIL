import sys

sys.stdin = open('input.txt')

T = int(input())
num = 1
arr = [[0] * 300 for _ in range(300)]
for i in range(1, 300):
    x, y = 1, i
    for j in range(i):
        arr[x][y] = num
        num += 1
        x += 1
        y -= 1

for tc in range(1, T + 1):
    p, q = map(int, input().split())
    x_1, x_2, y_1, y_2 = 0, 0, 0, 0

    for x in range(1, 300):
        for y in range(1, 300):
            if p == arr[x][y]:
                x_1 = x
                y_1 = y
            if q == arr[x][y]:
                x_2 = x
                y_2 = y
        if x_1 != 0 and x_2 != 0 and y_1 != 0 and y_1 != 0:
            break
    new_x = x_1 + x_2
    new_y = y_1 + y_2

    for x in range(1, 300):
        for y in range(1, 300):
            new = arr[new_x][new_y]

    print(f'#{tc} {new}')
