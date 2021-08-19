t = int(input())

for num in range(1,t+1):
    arr = list(input())
    sum = 0
    cnt = 0
    i = 0
    while i < len(arr):
        if arr[i] == '(' and arr[i+1] ==')':
            sum += cnt
            i+=2
        elif arr[i] =='(':
            cnt += 1
            i+=1
        elif arr[i] ==')':
            sum += 1
            cnt -= 1
            i += 1
    print(f'#{num} {sum}')

