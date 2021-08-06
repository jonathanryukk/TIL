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



