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