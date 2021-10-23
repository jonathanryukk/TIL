def find(s):
    global cnt
    Q = [s]
    memo[N] = 1
    while Q:
        for i in range(len(Q)):
            new = Q.pop(0)
            if new == M:
                return cnt
            cal = [new + 1, new - 1, new * 2, new - 10]
            for k in cal:
                if 1000000 >= k > 0 and not memo[k]:
                    memo[k] = 1
                    Q.append(k)
        cnt +=1



t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    memo = [False] * 1000001
    cnt = 0
    print(find(N))
