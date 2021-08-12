for num in range(1,11):
    A = int(input())
    LA = list(map(int,input().split()))
    cnt = 0

    for i in range(len(LA)-1, 0 ,-1): 
        for j in range(0, i):
            if LA[j] > LA[j+1]:
                LA[j] , LA[j+1] = LA[j+1] , LA[j]
    
    
    while cnt <A:
        LA[-1] -=1
        LA[0] +=1
        
        for i in range(len(LA)-1, 0 ,-1): 
            for j in range(0, i):
                if LA[j] > LA[j+1]:
                    LA[j] , LA[j+1] = LA[j+1] , LA[j]
        cnt += 1
    result = LA[-1]-LA[0]
    print(f'#{num} {result}')