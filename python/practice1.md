# practice1

* 최고점수 출력

```python
def max_score(scores):
    max1 = scores[0]
    for i in scores:
        if i > max1:
            max1 = i
    return max1
```



# practice2

* 특정점수 이상 출력

```python
def over(scores):
    count1 = 0
    for i in scores:
        if i > 60:
            count1 += 1
    return count1
```



# practice3

* 'menus' 에 항목 개수 

```python
def menu_count(restorant):
    count2 = 0
    for i in restorant['menus']:
        if bool(i) == True:
            count2 += 1
    return count2
```

```python
def menu_count(restorant):
    return(len(restorant['menus']))
```



# practice4

* 최소,최대값을 딕셔너리로 반환 

```python
def turn(temperatures):
    
    maximum=[]
    minimum=[]
    for i in temperatures:
        maximum.append(i[0])
        minimum.append(i[1])
    ans ={'maximum':maximum,
          'minimum':minimum}
    return ans
```



# practice5

* '비어있는 문자열' 이면 False

  그렇지않으면 True 반환하는 함수

```python
    if user_data['id']=='' or user_data['password']=='':
        return False
    else:
        return True
```



# practice6

* 아이디 마지막글자는 반드시 0~9 숫자로 끝나는 조건 만족하면 True

  그렇지 않으면 False 반환하는 함수

```python
def is_id_valid(user_data):
    try:
        psw=(user_data['id'][-1])
        int(psw)
        return True
    except ValueError:
        return False
```

