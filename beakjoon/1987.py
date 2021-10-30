def solve(x, y, l):
    global ans
    ans = max(ans, l)
    for d in range(4):
        i, j = x + dx[d], y + dy[d]
        if 0 <= i < r and 0 <= j < c and alpha[table[i][j]] == 0:
            alpha[table[i][j]] = 1
            solve(i, j, l + 1)
            alpha[table[i][j]] = 0


r, c = map(int, input().split())
table = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
alpha = [0] * 26
ans = 0
alpha[table[0][0]] = 1
solve(0, 0, 1)
print(ans)
