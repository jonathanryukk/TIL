t = int(input())
arr = []
for i in range(2, 10001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        arr.append(i)


for tc in range(1,t+1):
    n = int(input())

    cnt = 0
    while True:
        if n / 2 + cnt in arr:
            if n / 2 - cnt in arr:
                print(int(n / 2 - cnt), int(n / 2 + cnt))
                break
        cnt += 1
