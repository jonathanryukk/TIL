t = int(input())

for num in range(1,t+1):
    arr = input()
    ST = []
    sum1 = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            ST.append(arr[i])
        else:
            if arr[i-1] == '(':
                ST.pop()
                sum1 += len(ST)
            else:
                ST.pop()
                sum1 += 1

    print(sum1)
