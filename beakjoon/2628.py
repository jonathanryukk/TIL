import pprint

X, Y = map(int, input().split())
N = int(input())
arr = [[0] * (X + 1) for _ in range(Y + 1)]
for _ in range(N):
    X1, Y1 = map(int, input().split())
    if X1 == 0:
        for i in range(X + 1):
            arr[Y1][i] = 1
    if X1 == 1:
        for i in range(Y + 1):
            arr[i][Y1] = 1

pprint.pprint(arr)
