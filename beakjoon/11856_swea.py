t = int(input())

for tc in range(1, t + 1):
    a = input()
    a = set(list(a))
    if len(a) == 2:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
