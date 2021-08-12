a = input()

list_a = list(a)

cnt = 1

if len(list_a) == 1:
    if list_a[0] == ' ':
        print('0')

else: 
    for i in range(1,len(a)-1):
        if list_a[i] == ' ':
            cnt += 1
    print(cnt)

#경우의 수 4가지   앞에공백 뒤에공백 둘다공백  공백x