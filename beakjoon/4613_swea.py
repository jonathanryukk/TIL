t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    max_cnt = 0

    cntw = 0
    for a in range(n - 2):
        for b in range(m):
            if arr[a][b] == 'W':
                cntw += 1
        cntb = 0
        for c in range(a + 1, n - 1):
            for d in range(m):
                if arr[c][d] == 'B':
                    cntb += 1

            cntr = 0
            for e in range(c + 1, n):
                for f in range(m):
                    if arr[e][f] == 'R':
                        cntr += 1
            result = cntw + cntb + cntr
            if max_cnt < result:
                max_cnt = result

    print(f'#{tc} {(n*m)-max_cnt}')
