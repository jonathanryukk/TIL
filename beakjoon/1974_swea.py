import sys

sys.stdin = open('input1974.txt')


def check():
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            n_row = sdk[i][j]
            n_col = sdk[j][i]


            if row[n_row]:
                return 0
            if col[n_col]:
                return 0

            row[n_row] = 1
            col[n_col] = 1

            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = sdk[r][c]
                        if square[num]: return 0
                        square[num] = 1
    return 1

t = int(input())
for num in range(1, t + 1):
    sdk = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{num} {check()}')

