t = int(input())

for num in range(1,t+1):
    n = int(input())
    arr =[input().split() for _ in range(n)]

    dg90 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dg90[i].append(arr[n-1-j][i])
 
    dg180 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dg180[i].append(arr[n-1-i][n-1-j])

    dg270 = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dg270[i].append(arr[j][n-1-i])

    print(f'#{num}')
    for pair in zip(dg90, dg180, dg270):
        pair = list(pair)
        for i in range(3):
            pair[i] = ''.join(pair[i])

        print(*pair)