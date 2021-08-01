## 1110번

```python
A = int(input())
real_A = A
cnt =0
temp = 0
new = 0
while True:
    temp = A // 10 + A % 10 
    new = (A % 10)*10 + temp % 10
    A = new
    cnt = cnt +1
    if new == real_A:
        break
print(cnt)

  
```



## 2562번

```python
list1 = []

for i in range(9):
    list1.append(int(input()))

print(max(list1))
result = list1.index(max(list1))
print(result+1)
```

이 문제의 핵시!! 

list.index(a) - > a의 리스트 위치를 뽑아줌



## 10818번

```python
T = int(input())
list1 = list(map(int, input().split()))
print(min, max)
```



## 2577번

```python
A = int(input())
B = int(input())
C = int(input())

new = list(map(int, str(A*B*C)))

for i in range(0,10):
    print(new.count(i)) 
```



## 3052번

```python
list = []
for i in range(1,11):
    A = int(input())%42
    if A not in list:
        list.append(A)

print(len(list))
```



```python
nums = set()  # 중복되는 요소를 제거
for _ in range(10):
    i = int(input())
    nums.add(i%42)  # 집합자료형에 원소를 추가할 때 add 함수를 사용

print(len(nums))
```



## 1546번

```python
t = int(input())

list = list(map(int, input().split()))

max1 = max(list)

new_list = []

for i in range(t):
    new_list.append((list[i]/max1)*100)

AVG = sum(new_list)/ len(new_list)
print(AVG)
```



## 8958번

```python
t = int(input())

for i in range(t):
    a = input()
    result = 0
    sum = 0
    for j in a:
        if j =='O':
            sum = sum+1
            result = result+sum
        elif j == 'X':
            sum = 0
    print(result)

```

