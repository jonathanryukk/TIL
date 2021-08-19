import sys
sys.stdin = open('input.txt')

t = int(input())

for num in range(1,t+1):
    rating = ['A+','A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N,K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    list_sum=[]
    
    for i in range(N):
        sum = (arr[i][0] * 35) + (arr[i][1] * 45) + (arr[i][2] * 20) 
        list_sum.append(sum)
    
    real_rate = N//10

    new_list = sorted(list_sum, reverse=True)
    
    rate = (new_list.index(list_sum[K-1])) //real_rate

    print(f'#{num} {rating[rate]}')