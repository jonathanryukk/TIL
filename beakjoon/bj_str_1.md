## [파이썬에서 `str` 리스트를 문자열로 변환](https://www.delftstack.com/ko/howto/python/how-to-convert-a-list-to-string/#파이썬에서-str-리스트를-문자열로-변환)

`str.join()`메소드를 사용하여 `str` 데이터 타입 요소가있는리스트를 문자열로 변환 할 수 있습니다.

예를 들어

```python
A = ["a", "b", "c"]
StrA = "".join(A)
print(StrA)
## StrA is "abc"
```

`join` 메소드는 임의의 수의 문자열을 연결하며, 메소드가 호출 된 문자열은 주어진 각 문자열 사이에 삽입됩니다. 예제에서 볼 수 있듯이 빈 문자열 인 문자열 `""`은 목록 요소 사이에 삽입됩니다.

요소 사이에 공백을 추가하려면 다음을 사용해야합니다.

```python
StrA = " ".join(A)
## StrA is "a b c"
```



## [파이썬에서 비 `str` 목록을 문자열로 변환](https://www.delftstack.com/ko/howto/python/how-to-convert-a-list-to-string/#파이썬에서-비-str-목록을-문자열로-변환)

`join` 메소드에는 주어진 매개 변수로 `str` 데이터 유형이 필요합니다. 따라서 `int`형식 목록에 가입하려고하면 `TypeError` 가 표시됩니다.

```python
>>> a = [1,2,3]
>>> "".join(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    "".join(a)
TypeError: sequence item 0: expected str instance, int found
```

`int` 타입은 결합되기 전에 `str` 타입으로 변환되어야합니다.



### [리스트 내포](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

```python
>>> a = [1,2,3]
>>> "".join([str(_) for _ in a])
"123"
```



### [`map` 기능](http://book.pythontips.com/en/latest/map_filter.html#map)

```python
>>> a = [1,2,3]
>>> "".join(map(str, a))
'123'
```

`map` 함수는 `str` 함수를 목록 `a` 의 모든 항목에 적용하고 반복 가능한 `map` 객체를 반환합니다.

`"".join()`은 `map` 객체의 모든 요소를 반복하고 연결된 요소를 문자열로 반환합니다.



## 10809



```python
#  ord(아스키) > 아스키코드 반환 chr(숫자) -> 숫자>아스키
a = input()

list_a = list(a)

for i in range(97,123):
    if chr(i) in list_a:
        print(list_a.index(chr(i)),end=' ')
    else:
        print(-1,end=' ')

```



## 2675



```python
t = input()
for num in range(int(t)):
    a,b = input().split()

    for i in range(len(b)):
        for j in range(int(a)):
            print(b[i],end='')
    print('')
```



## 1157



```python
#str a를 대문자로 입력받기
a = input().upper()

# word라는 변수에 중복값을 줄인 list_a 를 저장
word = list(set(a))
#새로운 리스트 생성
new = []
# 반복문을통해 입력받은값에서 word 리스트의 요소가 몇번 반복되는지 new리스트에 저장
for i in word:
    count = a.count(i)
    new.append(count)
                    
# 만약 new의 최대값을 가진 수가 2개가 넘으면 ? 출력 아니면 new리스트에서 최댓값을가진 인덱스를 word에서 출력   
if new.count(max(new)) >= 2:
    print("?")
else:
    print(word[new.index(max(new))])
```



# 1152



```python
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
```





# 2908



숫자를 뒤집어서 더 큰 숫자 출력



```python
A,B = map(list,input().split())

ch_A = A[::-1]
ch_B = B[::-1]

real_A = "".join(map(str,ch_A))
real_B = "".join(map(str,ch_B))


if int(real_A) > int(real_B):
    print(real_A)
else:
    print(real_B)
```

# 



# 5622



```python
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()

result = 0

for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            result = result + dial.index(j) + 3


print(result)

#apple 01234 
```

