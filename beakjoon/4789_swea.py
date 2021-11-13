t = int(input())
for tc in range(1, t + 1):
    A = list(input())
    lenA = len(A)
    cnt = 0
    result = 0
    for i in range(lenA):
        if cnt < i:
            result += 1
            cnt += 1
        cnt += int(A[i])
    print(f'#{tc} {result}')
