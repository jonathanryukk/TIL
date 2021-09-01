t = int(input())

for tc in range(1, t + 1):
    a = int(input())
    if a % 2 == 1:
        print(f'#{tc} Odd')
    else:
        print(f'#{tc} Even')
