# 1274_SWEA

```python
t = int(input())

for i in range(1,t+1):
    P, Q, R, S, W = map(int,input().split())

    a = P*W
    if R > W:
        b = Q
    else:
        b = Q +(W-R)*S
    
    if a>b:
        print(f'#{i} {b}')
    else:
        print(f'#{i} {a}')
```





# 1989_SEWA

```python
t = int(input())

for i in range(1,t+1):
    A = input()
    if A == A[::-1]:
        print(f'#{i} {1}')
    else:
        print(f'#{i} {0}')
```

입력받은 A 와 A를 뒤집은게 같으면 1 아니면 0 출력





# 1959_SEWA

```python
T = int(input())

for i in range(1, T+1):
    n, m =map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []


    if m > n:   #00+11 / 01+12
        for i in range(m - n + 1): #0 1
            result = 0
            for j in range(n): #0 1
                result += (a[j+i]*b[j])
            c.append(result)

    else:
        for i in range(n - m + 1): # 0 1
            result = 0
            for j in range(m): # 0 1
                result += (a[j+i]*b[j]) #00+11 / 10+21
            c.append(result)

    print(f'#{i} {max(c)}')
```

