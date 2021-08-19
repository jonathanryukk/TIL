def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (paper(n - 1) + 2 * paper(n - 2))


t = int(input())
for num in range(1, t + 1):
    n = int(input()) / 10
    print(f'#{num} {paper(n)}')
