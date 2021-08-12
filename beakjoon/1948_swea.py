t = int(input())

for i in range(1,t+1):
    a,b,c,d = map(int,input().split())
    sum1 = 0
    sum2 = 0
    if a == 1:
         sum1 = b
    elif a == 2:
         sum1 = 31+b
    elif a ==3:
         sum1 = 59+b
    elif a==4:
         sum1 = 90+b
    elif a==5:
         sum1 = 120+b
    elif a==6:
         sum1 = 151+b
    elif a==7:
         sum1 = 181+b
    elif a==8:
         sum1 = 212+b
    elif a==9:
         sum1 = 243+b
    elif a==10:
         sum1 = 273+b
    elif a==11:
         sum1 = 304+b
    elif a==12:
         sum1 = 334+b
    if c == 1:
        sum2 = d
    elif c == 2:
        sum2 = 31+d
    elif c ==3:
        sum2 = 59+d
    elif c==4:
        sum2 = 90+d
    elif c==5:
        sum2 = 120+d
    elif c==6:
        sum2 = 151+d
    elif c==7:
        sum2 = 181+d
    elif c==8:
        sum2 = 212+d
    elif c==9:
        sum2 = 243+d
    elif c==10:
        sum2 = 273+d
    elif c==11:
        sum2 = 304+d
    elif c==12:
        sum2 = 334+d
                                                                    

    print(f'#{i} {sum2-sum1+1}')
