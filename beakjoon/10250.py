t = int(input())

for tc in range(t):
    H, W, N = map(int, input().split())

    floor = N % H
    ho = N // H + 1
    if floor == 0:
        ho = N // H
        floor = H

    print(f'{floor*100+ho}')