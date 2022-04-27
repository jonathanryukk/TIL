## Entity란?

`Entity` 클래스는 DB의 테이블에 존재하는 Column들을 필드로 가지는 객체를 말한다. Entity는 **DB의 테이블과 1대 1로 대응되며,** 때문에 테이블이 가지지 않는 컬럼을 필드로 가져서는 안된다. 또한 Entity 클래스는 다른 클래스를 상속받거나 인터페이스의 구현체여서는 안된다.

예를 들어 post 라는 테이블이 title, content, author 라는 컬럼들을 가지고 있다면, 이에 대응하는 Entity 클래스 Post는

```java
@Entity
public class Post {
    private String title;
    private String content;
    private String author;
}
```

와 같이 post 테이블의 컬럼들을 필드로 가져야 한다.

JPA를 사용할 때 Entity 클래스에는 @Entity 어노테이션을 붙여서 Entity임을 명시해 줘야 하며, 내부의 필드에는 @Column, @Id 어노테이션 등을 사용한다. Entity는 외부에서 최대한 Entity의 Getter를 사용하지 않도록 내부에 로직을 구현하는데, 이 때 **Domain 로직만 구현하고 Presentation 로직은 구현하지 않는다.**

Entity의 Getter 사용을 최대한 피하라고 했지만, 기본적으로 Entity를 만들 때 Getter는 만들어줘야 한다. 그런데 이동욱님이 쓰신 책을 보니, Entity 클래스에서 `Setter`를 만드는 것은 피하라는 조언이 있었다.

일반적으로 자바 클래스를 만들때 private 필드들을 가지고 습관적으로 Getter와 Setter를 만들고는 하는데, 문제는 Setter의 사용이 Entity의 일관성을 해칠 수 있다는 것이다.

Setter를 무분별하게 사용하게 되면, Entity의 인스턴스 값들이 언제 어디서 변하는지 명확히 알 수 없다. 따라서 Setter 대신 다른 방법으로 필드에 값을 넣어 주는 것이 좋다. 그런데 일반적으로 생각할 수 있는 인스턴스의 생성 시점에 생성자로 필드에 값을 넣어주는 방법 또한 그다지 좋지 않은 방법일 수 있는데, 생성자에 현재 넣는 값이 어떤 필드인지 명확히 알 수 없고, 매개변수끼리의 순서가 바뀌더라도 코드가 모두 실행되기 전까지는 문제를 알 수 없다는 단점이 있기 때문이다.

따라서 `Builder` 패턴을 사용하는 것이 가장 좋다. 멤버 변수가 많아지더라도 어떤 값을 어떤 필드에 넣는지 코드를 통해 확인할 수 있고, 필요한 값만 집어넣는 것이 가능하기 때문이다.

##### Entity 클래스 생성 및 Builder 패턴 예시

```java
@Getter
@Entity
@NoArgsConstructor
public class Membmer member {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String name;
    private String email;
    @Column(length = 13, nullable = false)
    private String phoneNumber;
 
    @Builder
    public Member(long id, String name, String email, String phoneNumber) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }
}

// 사용 방법

Member member = new member.builder()
        .name("홍길동")
        .email("test@gmail.com")
        .phoneNumber("010-1234-5678")
        .build();
```

## DAO란?

`DAO`는 **Data Access Object**의 약자로, 실제로 DB에 접근하는 객체다. DAO는 프로젝트의 서비스 모델과 실제 데이터베이스를 연결하는 역할을 하며, JPA에서는 DB에 데이터를 CRUD 하는 `Repository` 객체들이 DAO라고 볼 수 있다.

엄밀히 말하면 Repository가 DAO를 대체한다고 보는 것이 맞는 것 같은데, DAO와 Repository 모두 DB에 직접 쿼리를 날려 CRUD를 하는 것은 동일하나, **개념적인 측면에서 차이**가 있는 것 같다. 참고 자료를 한번 가져와봤다.

> DAO와 REPOSITORY 모두 퍼시스턴스 로직에 대한 객체-지향적인 인터페이스를 제공하고 도메인 로직과 퍼시스턴스 로직을 분리하여 관심의 분리(separation of concerns) 원리를 만족시키는데 목적이 있다. 그러나 비록 의도와 인터페이스의 메소드 시그니처에 유사성이 존재한다고 해서 DAO와 REPOSITORY를 동일한 패턴으로 취급하는 것은 성급한 일반화의 오류를 범하는 것이다.
> DAO는 퍼시스턴스 로직인 Entity Bean을 대체하기 위해 만들어진 개념이다. DAO가 비록 객체-지향적인 인터페이스를 제공하려는 의도를 가지고 있다고 하더라도 실제 개발 시에는 하부의 퍼시스턴스 메커니즘이 데이터베이스라는 사실을 숨기려고 하지 않는다. DAO의 인터페이스는 데이터베이스의 CRUD 쿼리와 1:1 매칭되는 세밀한 단위의 오퍼레이션을 제공한다. 반면 REPOSITORY는 메모리에 로드된 객체 컬렉션에 대한 집합 처리를 위한 인터페이스를 제공한다. DAO가 제공하는 오퍼레이션이 REPOSITORY 가 제공하는 오퍼레이션보다 더 세밀하며, 결과적으로 REPOSITORY에서 제공하는 하나의 오퍼레이션이 DAO의 여러 오퍼레이션에 매핑되는 것이 일반적이다. 따라서 하나의 REPOSITORY 내부에서 다수의 DAO를 호출하는 방식으로 REPOSITORY를 구현할 수 있다.
> 출처 : http://egloos.zum.com/aeternum/v/1160846

솔직히 완벽히 이해되지는 않는다. 이 부분은 개념적으로 좀 더 공부가 필요할 것 같다.

## DTO란?

![img](https://velog.velcdn.com/images%2Fohzzi%2Fpost%2F4cec2790-be9f-4263-96ee-704325bbeac1%2Fspring-package-flow.png)

`DTO`는 **Data Transfer Object**의 약자로, 계층 간 데이터 교환 역할을 한다. DB에서 꺼낸 데이터를 저장하는 Entity를 가지고 만드는 일종의 Wrapper라고 볼 수 있는데, Entity를 Controller 같은 클라이언트단과 직접 마주하는 계층에 직접 전달하는 대신 DTO를 사용해 데이터를 교환한다.

DTO는 그저 **계층간 데이터 교환이 이루어 질 수 있도록 하는 객체**이기 때문에, 특별한 로직을 가지지 않는 순수한 데이터 객체여야 한다. 또한 DB에서 꺼낸 값을 DTO에서 임의로 조작할 필요가 없기 때문에 DTO에는 Setter를 만들 필요가 없고 생성자에서 값을 할당한다. 개인적으로는 생성자 또한 사용하지 않고 Entity처럼 Builder 패턴을 통해 값을 할당하는 것이 가장 좋은 것 같다.

#### Entity와 DTO를 분리하는 이유

Entity의 값이 변하면 Repository 클래스의 Entity Manager의 flush가 호출될 때 DB에 값이 반영되고, 이는 다른 로직들에도 영향을 미친다. 때문에 View와 통신하면서 필연적으로 **데이터의 변경이 많은 DTO 클래스를 분리**해주어야 한다.

또한 도메인 설계가 아무리 잘 되었다 해도 Getter만을 이용해서 원하는 데이터를 표시하기 어려운 경우가 발생할 수 있는데, 이 경우에 Entity와 DTO가 분리되어 있지 않다면 Entity 안에 Presentation을 위한 필드나 로직이 추가되게 되어 객체 설계를 망가뜨리게 된다. 때문에 이런 경우에는 분리한 DTO에 Presentation 로직 정도를 추가해서 사용하고, Entity에는 추가하지 않아서 도메인 모델링을 깨뜨리지 않는다.

#### DTO와 VO와의 차이

VO(Value Object)도 DTO와 동일한 개념이다. 다만 DTO와의 차이는, DTO는 데이터를 계층간 교환(Transfer)하는데 의미가 있고, VO는 읽기만 가능한 **read-only** 속성을 가진 객체로서 데이터 그 자체에 의미를 두고 있다는 점이다.

> 참고자료
> https://gmlwjd9405.github.io/2018/12/25/difference-dao-dto-entity.html
> http://egloos.zum.com/aeternum/v/1160846
> https://iri-kang.tistory.com/5