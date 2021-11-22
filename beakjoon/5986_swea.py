a = [False, False] + [True] * (1000)
primes = []

for i in range(2, 1000):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 1000, i):
            a[j] = False

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    cnt = 0
    for x in range(len(primes)):
        if primes[x] < n:
            for y in range(x, len(primes)):
                if primes[x] + primes[y] < n:
                    for z in range(y, len(primes)):
                        if primes[x] + primes[y] + primes[z] == n:
                            cnt += 1
    print(f'#{tc} {cnt}')
