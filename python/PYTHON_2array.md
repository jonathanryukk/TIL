# 2차원배열



```python
N,M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

# 2 3 
# 1 2 3
# 4 5 6
```



* 빈 2차원 배열

```python
arr2 = [[0] * M for _ in range(N)]


```





# 배열 순회



### * 행 우선 순회

```python
for i in range(len(Array)) # 행의 수
	for j in range(len(Array[0])) # 열의 수
    	Array[i][j]
```



### * 열 우선 순회

```python
for j in range(len(Array)) # 행의 수
	for i in range(len(Array[0])) # 열의 수
    	Array[i][j]
```



### * 지그재그 순회

```python
for i in range(len(Array)) # 행의 수
	for j in range(len(Array[0])) # 열의 수
    	Array[i][j + (m-1-2*j) * (i % 2)]
```



### * 델타를 이용한 2차 배열 탐색

#### 4방향 인접배열요소 탐색 방법



```python
arr[0...n-1][0...n-1]
dx[] = [0,0,-1,1]
dy[] = [-1,1,0,0]   # <  > ∧ ∨


```



```python
t = int(input())

for num in range(1,t+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    sum = 0

    for i in range(N):
        for j in range(N):
            sum1 = 0
            for k in range(4):
                newi = i + dx[k]
                newj = j + dy[k]
                if 0 <= newi < N  and 0 <= newj < N:
                    sum1 += abs(arr[newi][newj] - arr[i][j])
            sum += sum1

    print(f'#{num} {}sum})
```

#### 달팽이

![image-20210812104655831](md-images/image-20210812104655831.png

![image-20210812112559494](md-images/image-20210812112559494.png)

### 전치 행렬

```python
for i in range(n):
    for j in range(m):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

대각선을 기준으로 각 행,열을 바꾸는 행렬





### 부분집합 생성하기

* 각 집합의 원소가 n개 일때 공집합을 포함한 부분집합의 수는 2^n개이다.

  ![image-20210811105546663](C:/Users/%EB%A5%98%ED%98%84%EC%A7%84/AppData/Roaming/Typora/typora-user-images/image-20210811105546663.png)



```python
t = int(input())

for num in range(1,t+1):
    arr = list(map(int, input().split()))

    sum1 = 0

    for i in range(10):
        for j in range(10):
            if arr[i] + arr[j] == 0:
                sum1 += 1

    if sum1 >= 1:
        print(f'#{num} 1')
    else:
        print(f'#{num} 0')
```



## 비트연산자



| Operator | Description                                                  | Example                   |
| :------- | :----------------------------------------------------------- | :------------------------ |
| &        | AND 연산. 둘다 참일때만 만족                                 | (a & b) = 12 → 0000 1100  |
| \|       | OR 연산. 둘 중 하나만 참이여도 만족                          | (a \| b) = 61 → 0011 1101 |
| ^        | XOR 연산. 둘 중 하나만 참일 때 만족                          | (a ^ b) = 49 → 0011 0001  |
| ~        | 보수 연산.                                                   | (~a) = -61 → 1100 0011    |
| <<       | 왼쪽 시프트 연산자. 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동 | a << 2 = 240 → 1111 0000  |
| >>       | 오른쪽 시프트 연산자. 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동 | a >> 2 = 15 → 0000 1111   |





# 검색



## * 순차검색

####  일렬로 되어있는 자료를 순서대로 검색

->가장 간단하고 직관적이지만 시간이 오래걸림

#### 두가지가 있는경우

-> 정렬되어 있지 않은 경우

 

-> 정렬되어 있는 경우 

키값보다 찾으려는 원소가 커지면 종료

찾으려는값이 인덱스 가장 큰값보다 크면 바로 종료



## * 이진검색 알고리즘

#### 자료이 한 가운데 있는 항복과 키 값을 비교하여 검색, 위치결정 -> 검색지속

#### 범위를 반씩 줄여가며 빠르게 검색수행 (자료가 정렬되어 있어야함)



 ```python
 start = 0
 end = len -1
 
 middle = st+end //2
 	if  a middle == key
     	return true
     elif a middle > key:
         end = middle - 1
     else 
     	start = middle +1
 ```





#### * 재귀 함수 이용

나중에 배움

