t = int(input())

for num in range(1,t+1):
    n = int(input())
    n_list = list(map(int,input().split()))
    n_list = n_list[::-1]
    result = 0
    max_n = n_list[0]
    
    for i in range(1,n):
        if n_list[i] < max_n:
            result += (max_n - n_list[i])
        else:
            max_n = n_list[i]
    print(f'#{num} {result}')