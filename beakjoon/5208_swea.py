t = int(input())


def find(x):
    global cntmax, cnt
    if x >= len(arr):
        if cntmax >= cnt:
            cntmax = cnt
        return

    if cntmax <= cnt:
        return

    for i in range(x + arr[x], x, -1):
        cnt += 1
        find(i)
        cnt -= 1


for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = arr[0]
    cntmax = 500
    cnt = 0
    find(1)

    print(f'#{tc} {cntmax-1}')
