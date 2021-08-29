import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    N, M, K = map(int, input().split())

    arr = list(map(int, input().split()))
    arr = sorted(arr)

    result = 'Possible'

    for i in range(N):
        cnt = (arr[i] // M) * K - (i + 1)
        if cnt < 0:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')
