change = [500, 100, 50, 10, 5, 1]

A = 1000 - int(input())

cnt = 0

while A > 0:
    for i in change:
        if A == 0:
            break
        else:
            cnt += (A // i)
            A = A % i

print(cnt)
