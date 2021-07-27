

# 데이터구조







## 문자열

* 변경할수 없고 순서가 있고 순회 가능하다.(반복가능) 
* 문자열 인덱스 0 1 2, -3 -2 -1



#### 문자열자르기

> ##### s[srart:stop:step



#### 문자열 조회/탐색

* .find 

x번째 위치를 반환, 없으면-1

```python
'apple'.find(p)
->1
'apple'.find(k)
->-1
```



* .index(x)

x번째 위치를 반환,없으면 ValueError 일으킴

```python
'apple'.index(p)
->1
'apple'.index(z)
->?value error
```



* .replace(old,new[,count])

바꿀 대상 글자(old)를 새로운 글자(new)로 바꿔서 반환(복사본 반환)

count를 지정하면, 해당 개수만큼 시행

```python
'coone'.replace('o','a')
->caane
'wooooowoo'.replace('o','!', 2)
->w!!ooowoo
```



* .strip([chars])

특정한 문자를 지정하면, 양쪽을 제거하거나, 왼쪽,오른쪽을 제거

기본값은 공백제거

```python
.rstrip()
.lstrip('h')  # (사이의 모든 문자 h를 지움 )

'안녕하세요????'.rstrip('?')
->'안녕하세요'
```



* .split(sep=none)

문자열을 특정한 단위로 나눠  리스트로 반환

```python
'a,b,c'.split('_')
['a,b,c']
'a,b,c'.split()
['a', 'b', 'c']
```



* 'separator'.join(iterable)

```python
'!'.join('ssafy')
's!s!a!f!y'

' '.join(['3','5'])
'3 5'
```



> capitalize() : 첫문자 대문자, 나머지는 소문자
>
> .title() : '나 공백 이후의 단어 첫 문자를 대문자로  
>
> .upper() : 모든 문자를 대문자로 바꾸기
>
> .lower() : 모두 소문자로
>
> .swapcase() : 대> 소  소 < 대문자 전환



* 내장함수 is -> 반환 True or False

> .isalpha()  : 알파벳 문자 여부
>
> .isupper() : 대문자 여부
>
> .islower() : 소문자 여부
>
> .istitle() : 타이틀 형식 여부



## 리스트

>  순서가 있는 시퀀스, 인덱스로 접근
>
> 특징 변겅가능하고 순서가 가능하고 순회가 가능함.



### 값추가 및 삭제



* append(x)

리스트 끝에 값을 추가

* extend(iterable)

리스트에 항목들이 추가됨

```python
cafe = ['a','b','c']
cafe.extend['coffee']
-> ['a', 'b', 'c,' 'c','o','f','f,'f','e',e',']
    


```

* .insert(i,x)

i 위치에 x를 추가함 리스트 길이보다 i가 클 경우 맨 뒤에 삽입



* .remove(x)

리스트에서 값이 x인 첫번째 항목 삭제, x가 없을경우 ValueError 발생



* .pop(i)

정해진위치 i에 있는 값을 삭제하고 그 항목을 반환함

i가 지정되지 않으면 마지막 항목을 삭제하고 반환



* .clear()

모든 항목을 삭제 (리스트를 비움)





### 탐색 및 정렬



* .index(x)

첫번째 x 값을 찾아 index 값을 반환



* .count(x)

원하는 값 x의 개수를 반환함



* .sort()

원본리스트를 정렬함 ,None 반환

sorted함수와 비교

``` N
numbers = [3,2,5,1]
result = numbers.sort()
print(numbers, result)
> [1,2,3,5] None   >원본 변경

numbers = [3,2,5,1]
result = solted(numbers)
 [3,2,5,1] [1,2,3,5]   >원본변경없이 복사본 제공
```



* .reverse()

순서를 반대로 뒤집음 (정렬x)



### 리스트 복사



![image-20210726103310328](md-images/image-20210726103310328.png)

* 얕은복사 (sliice) or iist() 를 활용하여 원본과 다른주소에 복사 가능

ex) b = list(a)





* List comprehension

1~3의 세제곱 결과가 담긴 리스트 만들기

```python
cubic_list = []
fori in range(1,4):
    cubic_list.append(number **3)
cubic_list = [1, 8, 27]


[number**3 for i in range(1,4)]
```



```python
[x for x in range(1,4) if x % 2 ==0] 
```





## Biult - in Function -map



#### map(function,iterable)

순회 가능한 데이터구조의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환

```python
num = [1,2,3]
result = map(str,num)
print(result, type(result))

['1','2','3']
```



#### filter(function,iterable)

순회 가능한 데이터구조의 모든 요소에 함수를 적용하고,

 그결과가 True인 것들을 반환

```python
def odd(n):
    return n%2
num = [1,2,3]

result = filter(odd,num)
list(result)    #형변환 필수!!!
->[1,3]

```





## 세트  {}

* 중복없이 순서가 ㅇ벗는 데이터구조
* 변경가능하고 순서가 없고 순회 가능하다.



* .add

세트에 값을 추가



* .update(*orhers)

여러개 값을 추가



* .remove()

세트에서 삭제하고 없으면 에러



* .discard

세트에서 삭제하고 없어도 에러 x



* .pop()

임의의 원소를 제거해 반환



## 딕셔너리

> Key와 Value로 구성
>
> 변경가능, 순서가 없고,  순회가능 



* .get(key[,default])

key에 대응하는 value를 가져옴

key가 딕셔너리에 없어도 default를 돌려줌(기본값은 None)



* .pop(key[,default])



* .update()

값을 제공하는 키,밸류로 갱신 (덮어쓰기)

![image-20210726112559398](md-images/image-20210726112559398.png)



> ### 딕셔너리 순회

딕셔너리는 기본적으로 key를 순회!!!!!!!

![image-20210726112718098](md-images/image-20210726112718098.png)





![image-20210726112752284](md-images/image-20210726112752284.png)



>### 반복가능하며 각각의요소는 튜플!!!!







