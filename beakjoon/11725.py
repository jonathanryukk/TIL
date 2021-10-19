n = int(input())
lst = [1]
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    if a in lst:
        lst.append(b)
        arr[a][b] = 1
    else:
        lst.append(a)
        arr[b][a] = 1

for j in range(1,n+1):
    for i in range(1,n+1):
        if arr[i][j] ==1:
            print(i)