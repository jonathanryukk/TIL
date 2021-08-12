# A = 동전의 갯수 B = 돈
A,B = map(int,input().split())

coins = []

for i in range(A):
    coins.append(int(input()))

coins =sorted(coins,reverse=True)

cnt = 0

for i in coins:
    coin_cnt = B//i
    B -= (coin_cnt*i)
    cnt += coin_cnt 

print(cnt)
