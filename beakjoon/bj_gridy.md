## 11047



```python
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

```



## 2839

```python
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

```





## 11399



```python
t = int(input())

list_i = list(map(int, input().split()))

list_i2 = sorted(list_i)

result = 0

for i in range(t,0,-1):
    result += i * list_i2[t-i] 

print(result)
```

