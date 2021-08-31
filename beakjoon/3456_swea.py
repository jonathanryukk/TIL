t = int(input())

for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    d = 0
    if a == b:
        d = c
    elif a == c:
        d = b
    elif b == c:
        d = a

    print(f'#{num} {d}')