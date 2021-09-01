T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    result = [0] * N

    for i in range(1,Q+1):
        L, R = map(int, input().split())

        for j in range(L-1, R):
            result[j] = i

    print("#{}".format(tc),end=' ')

    for i in range(N):
        print(result[i],end=' ')
    print()