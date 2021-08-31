import sys

sys.stdin = open('inpu.txt')

for tc in range(1, 11):
    arr = [list(map(int, input().split())) for _ in range(100)]
    max1 = 0
    sum3 = 0
    sum4 = 0
    for i in range(100):
        sum3 += arr[i][i]
        sum4 += arr[100 - i - 1][i]
        sum1 = 0
        sum2 = 0
        for j in range(100):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        if sum1 > max1:
            max1 = sum1
        if sum2 > max1:
            max1 = sum2
        if sum3 > max1:
            max1 = sum3
        if sum4 > max1:
            max1 = sum4

    print(f'#{tc} {max1}')
