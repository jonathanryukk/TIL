import itertools

t = int(input())

for tc in range(1, t + 1):
    result = 0
    a, b = input().split()
    a = list(a)
    b = list(b)

    for i in range(len(a), -1, -1):
        arr = itertools.combinations(a, i)
        cnt = 0
        for j in list(arr):
            j = list(j) #조합 큰거부터 순서대로
            if result > len(j):
                break
            for x in j: # j 첫번째 인자부터 검사
                for k in range(len(b)): #
                    if b[k] == x:
                        cnt += 1
                        pass
                    else:
                        break
                if cnt == len(j):
                    if result < cnt:
                        result = cnt
    print(f'#{tc} {result-1}')
