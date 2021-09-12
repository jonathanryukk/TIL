import sys

sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    arr = [list(map(int, list(input().split()))) for _ in range(9)]

    result = 1

    for i in range(9):
        sum1 = 0
        count1 = [0] * 9
        count2 = [0] * 9
        for j in range(9):
            count1[arr[i][j] - 1] = 1
            count2[arr[j][i] - 1] = 1
        for k in range(9):
            if count1[k] != 1 or count2[k] != 1:
                result = 0
                break

    for i in range(9):
        for j in range(9):
            count3 = [0] * 9
            if (i == 0 and j == 0) or (i == 3 and j == 3) or (i == 6 and j == 6):
                for x in range(3):
                    for y in range(3):
                        count3[arr[i + x][j + y] - 1] = 1
                for k in range(9):
                    if count3[k] != 1:
                        result = 0
                        break

    print(f'#{tc} {result}')
