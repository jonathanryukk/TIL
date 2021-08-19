t = int(input())

for num in range(1,t+1):
    x = input()
    y = input()
    max1 = 0
    for i in range(len(x)):
        cnt = 0
        for j in range(len(y)):
            if x[i] == y[j]:
                cnt += 1
            if cnt > max1:
                max1 = cnt
    print(f'#{num} {max1}')            