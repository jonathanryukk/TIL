t = int(input())

for num in range(1,t+1):
    lst = list(map(int, input().split()))
    for i in range(0, 2** len(lst)):
        sumV = 0
        for j in range(len(lst)):
            r = i & (1 << j)
            if r!=0:
                sumV += lst[j]
            else:
                print('0')