t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    sumlist = []
    for a in range(n):
        for b in range(n):
            if a != b and b != a + 1 and b != a - 1:
                for c in range(n):
                    if a != c and b != c and c != a + 1 and c != a - 1 and c != b - 1 and c != b + 1:
                        for d in range(n):
                            if a != d and b != d and c != d and d != a + 1 and d != a - 1 and d != b + 1 and d != b - 1 and d != c + 1 and d != c - 1:
                                if (a == n - 1 and b == 0) or (c == n - 1 and d == 0):
                                    if a < b and c < d:
                                        if a < c < b and a < d < b:
                                            sumlist.append(((lst[a] + lst[b]) ** 2) + ((lst[c] + lst[d]) ** 2))
                                        elif a > c > d or b < c < d or c < a < b < d:
                                            sumlist.append(((lst[a] + lst[b]) ** 2) + ((lst[c] + lst[d]) ** 2))

    print(f'#{tc} {max(sumlist)}')

# 5
# 10
# 80 90 65 55 90 60 40 35 30 25
# 8
# 30 25 70 55 95 75 90 20
# 10
# 60 85 45 25 15 70 55 70 85 35
# 15
# 80 30 35 95 45 85 30 25 100 85 10 60 80 30 5
# 20
# 45 30 5 85 55 85 10 5 75 60 15 65 45 50 75 80 15 10 50 90


# 1 38425
# 2 44225
# 3 37925
# 4 64850
# 5 57850
