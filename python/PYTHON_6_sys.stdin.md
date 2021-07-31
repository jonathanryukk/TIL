

# **input과 sys.stdin.readline의 차이점**



일단 sys.stdin.readline()과 input()은 같은 역할을 하지 않는다.

 

**input() 내장 함수는 parameter로 prompt message를 받을 수 있다.** 따라서 입력받기 전 prompt message를 출력해야 한다. 물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다. **하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.**

 

**또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다.** 즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다. **반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다.** 이 때문에 조금 귀찮은 점이 있기도 하다.

 

### **결론**                       

결론적으로 input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.









```python
import sys
T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
```

```python
T = int(input())
for i in range(T):
   a, b = map(int, input().split())
   print(a + b)
```





## input()대신 sys.stdin.readline()을 사용하는 이유

한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 `input()`으로 입력 받는다면 시간초과가 발생할 수 있습니다. 대표적인 예시가 백준 BOJ 15552번 문제입니다.

![img](https://media.vlpt.us/images/yeseolee/post/8fb3302c-b3dd-451c-80c3-d84c60ae6e60/K-20210115-184755.png)

```python
import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
```

맨 첫줄 Test case를 입력받을 때는 `input()`을 사용해도 무방합니다.
그러나 반복문으로 여러줄 입력받는 상황에서는 반드시 `sys.stdin.readline()`을 사용해야 시간초과가 발생하지 않습니다.

### 

```python
import sys
a = int(sys.stdin.readline())
```

😨 그냥 `a = sys.stdin.readline()` 하면 안되나요?
👉 `sys.stdin.readline()`은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
만약 `3`을 입력했다면, `3\n` 이 저장되기 때문에, 개행문자를 제거해야 합니다.
또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.

### 

```python
import sys
a,b,c = map(int,sys.stdin.readline().split())
```

`map()`은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수입니다.
위와 같이 사용한다면 a,b,c에 대해 각각 int형으로 형변환을 할 수 있습니다.



###  임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때

```python
import sys
data = list(map(int,sys.stdin.readline().split()))
```

`split()`은 문자열을 나눠주는 함수입니다.
괄호 안에 특정 값을 넣어주면 그 값을 기준으로 문자열을 나누고, 아무 값도 넣어주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눕니다.

`list()`는 자료형을 리스트형으로 변환해주는 함수입니다.
`map()`은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 `list()`로 감싸주었습니다.



###  임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때

```python
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
```

이렇게 한다면 각 요소의 길이가 동일한 2차원 리스트도 만들 수 있고,
각각 길이가 다른 2차원 리스트도 입력 받을 수 있습니다.



###  문자열 n줄을 입력받아 리스트에 저장할 때

```python
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
```

`strip()`은 문자열 맨 앞과 맨 끝의 공백문자를 제거합니다.

