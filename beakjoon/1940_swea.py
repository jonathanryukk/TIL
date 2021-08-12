t = int(input())

for num in range(1,t+1):
    t1 = int(input())

    v = 0
    d = 0

    for i in range(t1):
        list_a = list(map(int, input().split()))

        if list_a[0] == 0:  #그대로
            v = v
            d += v
        elif list_a[0] == 1: #가속
            v += list_a[1]
            d += v
        else:  #감속
            if list_a[1] > v:
                v = 0
                d = d
            else:
                v -= list_a[1]
                d += v
    print(f'#{num} {d}')


