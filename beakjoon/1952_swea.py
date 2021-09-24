t = int(input())

for tc in range(1, t + 1):
    price = [0] * 13
    A, B, C, D = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    for i in range(1, 13):
        price[i] = min(plan[i] * A, B) + price[i - 1]
        if i > 2:
            price[i] = min(price[i], C + price[i - 3])
    result = min(price[12], D)
    print(f'#{tc} {result}')
