t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arrN = []

    for i in range(1, N + 1):
        arrN.append(i)

    for i in arr:
        arrN.remove(i)

    result = " ".join(map(str, arrN))
    print(f'#{tc} {result}')
