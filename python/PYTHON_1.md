# PYTHON_1





## 실수 비교

```python
num1 = 0.1 * 3
num2 = 0.3
import math 
math.isclose(num1,num2)
```



## 단어제거 후 출력

```python
word = input()

for i in word:
    if i == 'a':
        pass
    else:
        print(i,end='')
```



## 단어 뒤집기

```python
word = input()
lens = len(word)

for i in range(lens,0,-1):
    print(word[i-1],end='')
```



## Dicitionary 만들기

```python
dic1 = {'이름' : '나이'}

print(dic1)
```



## 반복문으로 네모 출력

```python
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print('*',end='')
    print()
```



## 조건표현식 : 삼항연산자

```python
temp = 36.5
if temp >= 37.5:
    print("입실 불가")
else:
    print("입실 가능")
    
###3항연산자로 바꾸기###

temp = float(input())

print('입실가능') if temp <= 37.5 else print('입실불가')

```



## 평균 구하기

```python
scores = [80, 89, 99, 83]
sum1 = 0

for i in range(len(scores)):
    sum1 = sum1 + scores[i]

print(sum1/4)
```



## 중간 값 찾기 (sort)

```python
numbers = [
         85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
         51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
         52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
     ]
lens = len(numbers)

sort1=sorted(numbers)

print(sort1[lens//2])

```



## 계단 만들기

```python
number = int(input())

# 아래에 코드를 작성하시오.
for i in range(number):
    for j in range(i+1):
        print(j+1,end='')
        if j == i:
            print()

```

