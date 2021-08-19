t = int(input())
for num in range(1,t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    change_arr=[]
    result_arr=[]

    for i in range(n): 
        for j in range(n-m+1): 
            if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                result = ''.join(arr[i][j:j+m])

    for i in range(n):
        for j in range(n):
            change_arr += arr[j][i]
        result_arr.append(''.join(change_arr))

    for i in range(n): 
        for j in range(n-m+1): 
            if result_arr[i][j:j+m] == result_arr[i][j:j+m][::-1]:
                result = ''.join(result_arr[i][j:j+m])

    print(f'#{num} {result}')

