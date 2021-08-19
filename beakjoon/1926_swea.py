n = int(input())
arr = [str(i) for i in range(1,n+1)]

for i in range(n):
    cnt = 0
    if '3' in arr[i]:
        cnt += arr[i].count('3')
    if '6' in arr[i]:
        cnt += arr[i].count('6')
    if '9' in arr[i]:
        cnt += arr[i].count('9')
    arr[i] = '-'*cnt
    
    if cnt == 0:
        arr[i] = str(i+1)

print(' '.join(arr))
