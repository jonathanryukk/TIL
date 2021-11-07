a = [False, False] + [True] * (1000)
primes = []

for i in range(2, 1000):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 1000, i):
            a[j] = False

t = int(input())


def find(x, sumv):
    global n
    if sumv == n:
        cnt += 1
        return
    if (sumv > n) and x >= 1000:
        return
    else:
        find(primes[x + 1], sumv + primes[x])
        find(primes[x], sumv + primes[x])
        find(primes[x + 1], sumv)


for tc in range(1, t + 1):
    n = int(input())
    cnt = 0

    find(0, 0)

    print(f'#{tc} {cnt}')
