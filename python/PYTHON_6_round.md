## **1. 파이썬 round 함수로 소수점 관리하기**

------

예전 파이썬 반올림 round 포스팅에서 언급을 한번 하긴 했지만, 소수점 자리수 관련한 예제를 들지는 않았던 것 같네요.

**round(반올림하고자 하는 값)**

이런 방식으로 round 함수를 사용할 수 있습니다. 하지만 우리에겐 round 두 번째 인자가 있습니다.

**round(반올림하고자 하는 값, 자릿수)**

기본적으로 자릿수에 아무것도 넣지 않는다면
3.1311 이런 식으로 소수점이 들어갔을 때 소수점 첫째 자리에서 바로 반올림이 되어서 3인 값이 나오게 됩니다.

하지만 자릿수를 건드려주면 소수점 조절을 해서 반올림을 할 수 있습니다. 
바로 예제를 보시죠

```
a = round(1.23456)
b = round(1.23456, 0)
c = round(1.23456, 1)
d = round(1.23456, 2)
e = round(1.23456, 3)
f = round(1.23456, 4)

print(f"round(1.23456) : {a}")
print(f"round(1.23456, 0) : {b}")
print(f"round(1.23456, 1) : {c}")
print(f"round(1.23456, 2) : {d}")
print(f"round(1.23456, 3) : {e}")
print(f"round(1.23456, 4) : {f}")
```



![img](https://blog.kakaocdn.net/dn/buPwqz/btq6na3jiZU/lvxLoAQIKekycwnuvx8kk1/img.png)



이런 식으로 반올림 함수인 round의 두 번째 인자를 이용해서 구하고자 하는 소수점에서 반올림을 할 수 있습니다.

round 함수에 대해서 자세한 설명이 필요하다면 [[바로가기\]](https://blockdmask.tistory.com/418) 해당 포스팅에서 확인해주세요

 

 

## **2. 파이썬 format 서식 지정으로 소수점 관리하기**

------

우리가 숫자를 출력할 때 서식 문자를 통해서도 소수점을 조절할 수 있는데요.

우리가 format 함수를 이용할 때 이런 식으로 사용을 했었습니다.
**" 문자열 {} 블라블라 {} ".format(값1, 값2)**

이렇게 사용을 했는데, 앞에 있는 {} 중괄호 안에 소수점을 몇 개 출력할 것이라는 것을 알려주면 됩니다.

이렇게 말이죠.

**"이것을 문자열 { : .2f}".format(실수 입력)**

이런 식으로 사용하면 **{ : .2f } "소수점 2자리 까지만 출력하겠다." 라는 뜻이며,
**이것은 소수점 3번째 자리에서 반올림을 해서 2자리 까지 출력을 하게 됩니다.
: 콜론의 앞에는 format 인자의 번지를 입력하는 부분이고,
: 콜론 뒤에는 .숫자f 로 입력하면 숫자만큼의 자릿수까지 출력하겠다는 뜻입니다.

말로 하려니 어려우니, 바로 에제로 확인하시죠.

```
a = "format example1 : {:.2f}".format(1.23456789)
print(a)

b = "format example2 : {:.2f} / {:.3f}".format(1.23456789, 3.456789)
print(b)

c = "format example3 : {0:.2f} / {1:.1f}".format(3.22521321, 10.123456)
print(c)

d = "format example4 : {1:.2f} / {0:.1f}".format(3.22521321, 10.123456)
print(d)
```



![img](https://blog.kakaocdn.net/dn/sXsRA/btq6lZgMoG0/okkTM9PrU2GuaXPMqmmJMK/img.png)



이런 식으로 format 함수를 이용해서 소수점 자리를 관리할 수 있습니다.

 

해당 포스팅에서는 소수점을 조절하는 방법을 위한 포스팅이므로
**format 함수를 통한 문자열 출력 상세**는 [[바로가기\]](https://blockdmask.tistory.com/424) 해당 포스팅에서 확인하시면 됩니다.

 

 

## **3. 파이썬 f-string에서 소수점 관리하기** 

------

f-string의 방법은 위 format에서 배웠던 방식이랑 동일합니다.

**f'이것은 문자열 {변수 : 0.2f} 입니다'**

위와 같이 f-string을 나타 낼 수 있게 문자열 앞에**f를** 입력하고 
**중괄호 사이에 {변수 : 소수점자리수}** 순서로 작성하면 됩니다.

```
num1 = 1.23456789
num2 = 9.87654321

print(f'f-string example1 : {num1:.0f}')
print(f'f-string example2 : {num1:.1f}')
print(f'f-string example3 : {num1:.2f}')
print(f'f-string example4 : {num1:.3f}')
print(f'f-string example5 : {num1:.4f}')

print(f'f-string example6 : {num2:.0f}')
print(f'f-string example7 : {num2:.1f}')
print(f'f-string example8 : {num2:.2f}')
print(f'f-string example9 : {num2:.3f}')
print(f'f-string example10 : {num2:.4f}')
```



![img](https://blog.kakaocdn.net/dn/4xRMl/btq6lnvyLFq/HQX8EFh3YoMNdrdhUy4woK/img.png)



이런 식으로 **f-string을 통해서 소수점을 간단하게 출력**할 수 있습니다.



출처: https://blockdmask.tistory.com/534 [개발자 지망생]