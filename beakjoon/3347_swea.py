t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    lst = [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            if A[j] <= B[i]:
                lst[j] += 1
                break
    tmp = max(lst)
    index = lst.index(tmp)

    print(f'#{tc} {index + 1}')
