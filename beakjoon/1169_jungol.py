N, M = map(int, input().split())
if M == 1:
    for i in range(1,7):
        for j in range(1, 7):
            for k in range(1, 7):
                print(i, j, k)
result = []
if M == 2:
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                a = sorted([i, j, k])
                if a not in result:
                    result.append([i, j, k])
                    print(i, j, k)
if M == 3:
    for i in range(1, 7):
        for j in range(1, 7):
            if j == i:
                break
            else:
                for k in range(1, 7):
                    if k != j and k != i:
                        print(i, j, k)
N, M = map(int, input().split())
path = [0 for  in range(N)]
used = [0 for  in range(7)]
def run1(lev):
    if lev == N:
        print(path)
        return
    for i in range(1, 7):
        path[lev] = i
        run1(lev+1)
def run2(lev, start):
    if lev == N:
        print(path)
        return
    for i in range(start, 7):
        path[lev] = i
        run2(lev+1, i)
def run3(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1, 7):
        if used[i] == 1:
            continue
        used[i] = 1
        path[lev] = i
        run3(lev + 1)
        used[i] = 0
if M == 1:
    run1(0)
elif M == 2:
    run2(0, 1)
elif M == 3:
    run3(0)