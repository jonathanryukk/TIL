A,B = map(int,input().split())

a = 0
while a > B:
    cnt = 0
    for i in range(1,B+1): 
        if B % i == 0:
            cnt+=1
    if cnt ==2:
        print(a)

    a= a+1