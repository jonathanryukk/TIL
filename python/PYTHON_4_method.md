# 메소드의 특징



**인스턴스 메소드는 클래스로 인스턴스를 선언 후 클래스 내부 메소드를 사용 가능**하고

**클래스 메소드와 스태틱 메소드는** **인스턴스를 선언하지 않아도 내부 메소드를 사용**

| 종류                | 설명                                                        | 사용 예시                                           | 특징                                                         | 선언방법                                             |
| ------------------- | ----------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| **Instance 메소드** | 클래스로 인스턴스를 선언 후 사용 가능                       | person_01 = Person('홍길동)  person_01.print_name() | 인스턴스 자신을 self로 전달                                  | 클래스 내에서 def print_name(self):                  |
| **Class 메소드**    | 클래스로 인스턴스를 선언하지 않아도 사용 가능               | Person.print_name('홍길동)                          | 클래스 자신을 cls로 전달                                     | 클래스 내에서 @classmethod def print_name(cls, name) |
| **Static 메소드**   | 인스턴스를 서언 후 사용해도 되고, 선언하지 않고 사용해도 됨 | Person.print_name('홍길동')                         | 인스턴스나 클래스에게 아무것도 전달받지 않음, 그냥 함수처럼 사용 가능 | 클래스 내에서 @staticmethod def print_anme(name)     |

 

### **예시 코드**

```
# 1. Instance 메서드 예시

class InstanceMethod(object):
    
    def __init__(self, name):
        self.name = name
    
    def introduce_myself(self):
        return '저는 {0}입니다.'.format(self.name)

inst_method = InstanceMethod('홍길동')
inst_method.introduce_myself()

>>> 저는 홍길동입니다.

# 2. Class 메서드 예시

class ClassMethod(object):
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def introduce_myself(cls, name):
        return '저는 {0}입니다.'.format(name)

ClassMethod.introduce_myself('홍길동')

>>> 저는 홍길동입니다.

# 3. Static 메서드 예시

class StaticMethod(object):
    
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def introduce_myself(name):
        return '저는 {0}입니다.'.format(name)

StaticMethod.introduce_myself('홍길동')

>>> 저는 홍길동입니다.
```



출처: https://mentha2.tistory.com/201 [행궁동 데이터 엔지니어]