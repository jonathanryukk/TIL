t = int(input())
n = 5
for num in range(1,t+1):
    arr = [input() for _ in range(5)]
    maxlen = 0
    for i in arr:
        if maxlen <= len(i):
            maxlen = len(i)
    
    for i in range(n):
        if len(arr[i]) < maxlen:
            while len(arr[i]) < maxlen:
                arr[i] +=' '

    print(f'#{num} ',end='')
    for i in range(maxlen):
        for j in range(n):
            print(arr[j][i].strip(),end='')
    print('')
    

