n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1
    for j in range(n):
        if arr[i][1] < arr[j][1] and arr[i][0] < arr[j][0]:
            rank+=1
    print(rank,end=' ')
