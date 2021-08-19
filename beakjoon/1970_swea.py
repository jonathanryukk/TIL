list1 = [50000,10000,5000,1000,500,100,50,10]

t = int(input())

for num in range(1,t+1):
    list2 = []
    money = int(input())
    for i in range(len(list1)):
        cnt = 0    
        cnt = money//list1[i] 
        list2.append(str(cnt))
        money = money%list1[i]
   
    print(f'#{num}')
    print(' '.join(list2))
