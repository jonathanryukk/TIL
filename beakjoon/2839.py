a= int(input())
cnt = 0

if a == 1 or a == 2 or a == 4 or a == 7:
    print('-1')

else:
    cnt = a//5
    if a%5 == 0:
        print(cnt)
    elif a%5 == 1:
        print(cnt+1)
    elif a%5 == 2:
        print(cnt+2)
    elif a%5 == 3:
        print(cnt+1)
    elif a%5 == 4:
        print(cnt+2)
