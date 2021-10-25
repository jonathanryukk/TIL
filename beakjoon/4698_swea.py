n = 1000000
lst = [False, False] + [True] * (n - 1)
for i in range(2, n + 1):
    if lst[i]:
        for j in range(2 * i, n + 1, i):
            lst[j] = False

t = int(input())

for tc in range(1, t + 1):
    d, a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b + 1):
        if str(d) in str(i) and lst[i] == True:
            cnt += 1

    print(f'#{tc} {cnt}')

