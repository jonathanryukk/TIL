# import sys
#
# sys.stdin = open('input.txt')
#

def S(x, y):
    if arr[x][y] == '^':
        for i in range(x, -1, -1):
            if arr[i][y] == '#':
                break
            elif arr[i][y] == '*':
                arr[i][y] = '.'
                break
    elif arr[x][y] == '>':
        for i in range(y, m):
            if arr[x][i] == '#':
                break
            if arr[x][i] == '*':
                arr[x][i] = '.'
                break

    elif arr[x][y] == '<':
        for i in range(y, -1, -1):
            if arr[x][i] == '#':
                break
            if arr[x][i] == '*':
                arr[x][i] = '.'
                break

    else:
        for i in range(x, n):
            if arr[i][y] == '#':
                break
            if arr[i][y] == '*':
                arr[i][y] = '.'
                break


def U(x, y):
    if x > 0:
        if arr[x - 1][y] == '.' and 0 <= (x - 1) < n:
            arr[x][y] = '.'
            arr[x - 1][y] = '^'
            return (x - 1), y
        else:
            arr[x][y] = '^'
            return x, y
    else:
        arr[x][y] = '^'
        return x, y


def D(x, y):
    if (n - 1) > x:
        if arr[x + 1][y] == '.' and 0 <= (x + 1) < n:
            arr[x][y] = '.'
            arr[x + 1][y] = 'v'
            return (x + 1), y
        else:
            arr[x][y] = 'v'
            return x, y
    else:
        arr[x][y] = 'v'
        return x, y


def L(x, y):
    if y > 0:
        if arr[x][y - 1] == '.' and 0 <= (y - 1) < m:
            arr[x][y] = '.'
            arr[x][y - 1] = '<'
            return x, (y - 1)
        else:
            arr[x][y] = '<'
            return x, y
    else:
        arr[x][y] = '<'
        return x, y


def R(x, y):
    if (m - 1) > y:
        if arr[x][y + 1] == '.' and 0 <= (y + 1) < m:
            arr[x][y] = '.'
            arr[x][y + 1] = '>'
            return x, (y + 1)
        else:
            arr[x][y] = '>'
            return x, y
    else:
        arr[x][y] = '>'
        return x, y


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    count = int(input())
    command = list(input())

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '>' or arr[i][j] == '<' or arr[i][j] == '^' or arr[i][j] == 'v':
                x, y = i, j
                break

    for z in command:
        if z == 'U':
            x, y = U(x, y)
        elif z == 'D':
            x, y = D(x, y)
        elif z == 'L':
            x, y = L(x, y)
        elif z == 'R':
            x, y = R(x, y)
        else:
            S(x, y)

    print(f'#{tc}', end=' ')
    for nx in arr:
        for ny in nx:
            print(ny, end='')
        print()


# **....v
# .-..#..
# #......