t = int(input())

for num in range(1,t+1):
    n,m = map(int, input().split())
    arr =[list(map(int, input().split())) for _ in range(n)]

    max1 = 0
    for x in range(n-m+1):
        for y in range(n-m+1):
            sum1 = 0
            for i in range(m):
                for j in range(m):
                    sum1 += arr[i+x][j+y]
            if sum1 > max1:
                max1 = sum1

    print(f'#{num} {max1}')