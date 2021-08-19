A = list(range(1, 13))
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = 0

    for j in range(1 << 12):
        count1 = 0
        sum1 = 0
        for k in range(12):
            if j & (1 << k):
                sum1 += A[k]
                count1 += 1
        if count1 == a and sum1 == b:
            result += 1

    print('#{} {}'.format(i + 1, result))

