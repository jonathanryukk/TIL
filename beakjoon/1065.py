t = int(input())
cnt = 0


for i in range(1,t+1):
    t_100 = i//100
    t_10 = (i%100)//10
    t_1 = (i%100)%10
    if i<100:
        cnt += 1
    elif t_10-t_1 == t_100-t_10:
        cnt += 1

print(cnt)