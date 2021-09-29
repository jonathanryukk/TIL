import sys

sys.stdin = open('input.txt')


def S(x, y):
    if arr[x][y] == '^':
        for i in range(x, -1, -1):
            if arr[i][y] == '#':
                break
            elif arr[i][y] == '*':
                arr[i][y] = '.'
                break
    elif arr[x][y] == '>':
        for i in range(y, m + 1):
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
        for i in range(x, n + 1):
            if arr[x][i] == '#':
                break
            if arr[i][y] == '*':
                arr[i][y] = '.'
                break


def U(x, y):
    if arr[x - 1][y] == '.' and 0 <= (x-1) < n:
        arr[x][y] = '.'
        arr[x - 1][y] = '^'
        x -= 1
        return x, y
    else:
        arr[x][y] = '^'
        return x, y


def D(x, y):
    if arr[x + 1][y] == '.' and 0 <= (x+1) < n:
        arr[x][y] = '.'
        arr[x + 1][y] = 'v'
        x += 1
        return x, y
    else:
        arr[x][y] = 'v'
        return x, y


def L(x, y):
    if arr[x][y - 1] == '.' and 0 <= (y-1) < m:
        arr[x][y] = '.'
        arr[x][y - 1] = '<'
        y -= 1
        return x, y
    else:
        arr[x][y] = '<'
        return x, y


def R(x, y):
    if arr[x][y + 1] == '.' and 0 <= (y+1) < n:
        arr[x][y] = '.'
        arr[x][y + 1] = '>'
        y += 1
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

    for z in command:
        if z == 'U':
            U(x, y)
        elif z == 'D':
            D(x, y)
        elif z == 'L':
            L(x, y)
        elif z == 'R':
            R(x, y)
        else:
            S(x, y)

    print(arr)
