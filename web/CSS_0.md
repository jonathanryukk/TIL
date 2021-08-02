## CSS란

Cascading Style Sheets 의 줄임말로 documents가 사용자에게 어떻게 보여질까를 기술하는 언어이고 보통 HTML 문서를 시각적으로 꾸미는 용도로 사용한다.

css는 **선택자**, **선언**, **속성** 이렇게 세 가지로 이루어져 있다.
![img](https://media.vlpt.us/images/ljinsk3/post/ced8a825-0edd-432b-98fb-2180e0cd4b06/csss.png)

선택자는 html 문서상에서 각 태그들을 식별할 수 있게 붙여놓은 이름을 선택자로 활용할 수 있다.
ex) sematic tags, class("."), id("#")

## CSS 방법론

#### 작명 규칙(Naming Convention)

- 유지 보수를 위해서 해당 태그의 CSS 선택자는 최대한 명확한 의미를 드러낼 수 있도록 선택한다.
- 소문자, 숫자만을 이용하여 작명한다.
- 여러 단어의 조합은 '-'을 이용해서 작명한다.

#### 블록(Block)

- 재사용 할 수 있는 기능적으로 독립적인 페이지 구성 요소.
- HTML에서 블록은 class 속성으로 표시된다. 각 블록은 형태나 속성 (red, big)이 아닌 목적(menu, button)에 맞게 결정해야 한다.
- 각 블록은 환경에 영향을 받지 않아야 한다. (위치, 여백 등을 임의로 설정 하지 말자)

#### 요소(Element)

- 블록 안에서 특정 기능을 담당하는 부분
- block__element 형태로 네이밍한다.

### 수식어(Modifier)

- 블록이나 요소의 모양 또는 상태를 결정한다.
- block__element--modifier (더블 하이픈)으로 네이밍한다.

이렇게 기능별로 선택자 네이밍을 분리해놓으면, 각각의 선택자를 혼합해서 사용할 수 있고 중복되는 코드를 상당부분 줄일 수 있습니다.

```html
<!-- example --> 
<section class="name
  		name__comment 
                name__comment--color"> .... 
</section>
```

나중에 BEM 찾아서 더 공부하거나, SCSS를 공부해보면 css 파일을 효과적으로 관리할 수 있는데 많은 도움이 될 듯하다.

## 반드시 알아야 하는 CSS 속성들

`<head>` 안에서 style 태그를 정의하고 그 안에 문서 내다 다른 태그들을 선언하고 꾸민다고 가정해보자. 만약 태그와 속성내용이 많아지면 html 문서 길이는 기하급수적으로 길어지게 될 것이다.

외부에 별도의 css 파일을 만들고 거기에 style을 정의한 후 해당 css 파일을 link 태그로 html 문서에 import 해서 style을 적용시킬 수 있다.

보통 css나 js, image 파일들을 정적 파일들이라고 하는데 별도의 폴더를 만들어서 관리하게 된다.

`<head>` 부분에 다음과 같이 파일의 경로를 추가하면된다.

```html
<link rel="stylesheet" type="text/css" href="css/index.css" >
```

### font

페이지에서 사용할 폰트의 종류를 외부에서 받아올 수 있다. 부분마다 폰트를 사용할 수 있고 body 전체에 걸쳐서 특정 폰트를 사용하게 설정할 수 있다. 구글 폰트 페이지에서 import 하는 link를 가져와서 body에 적용시키면 쉽게 적용할 수 있다.

font 관련된 속성으로는 `font-size`, `font-weight`, `text-style` 등이 있습니다.

### box-model

HTML 요소는 박스 모델로 되어 있다. 태그를 통해 요소를 만들 때마다 새로운 box가 생기고 그 박스에 style을 주어서 문서를 꾸밀 수 있게 되는 것이다.

![img](https://media.vlpt.us/images/ljinsk3/post/ced97701-49cb-4127-80a5-580c78b9bc55/boxmodel.png)

내용을 표시하는 영역(Content Area)부터 바깥 영역 여백(Margin)까지를 한 박스 모델의 영역이라고 보면 된다.

##### width

- 내용을 표시하는 영역에서 가로 길이를 나타낸다.

##### height

- 내용을 표시하는 영역에서 세로 길이를 나타낸다.
- width와 height 을 구하는 기준은 기본이 위 그림이지만, `box-sizing` 속성을 통해서 `border-box`를 지정하면 테두리를 width와 height를 계산하는 기준으로 변경할 수 있다.

##### padding

- 내용과 border 사이의 영역을 나타내고 안쪽 여백 역할을 담당한다.

##### border

- 내용에 패딩을 더한 영역의 경계를 나타내며 margin과 padding의 경계가 되기도 한다. 테두리 역할을 한다.

##### margin

- border 부터 box model의 maximum 범위 까지를 나타내는 영역이다. 바깥 여백 영역 역할을 한다.
- 외부 요소와의 거리를 조절하는 용도로 많이 사용된다.

### display

display 속성은 요소를 어떻게 보여줄지를 결정한다. 주로 4가지 값이 쓰이는데 `none`, `block`, `inline`, `inline-block`이 쓰인다.

`none`은 아예 요소를 아예 보여주지 않고 지워버린다.

`block`은 기본적으로 가로영역을 전부다 차지하는 놈이다. 대표적으로 `div`, `p`, `h`, `li` 태그들이 그러한 때문에 요소 다음에 오는 요소는 개행이 된 것 처럼 보여진다. width, height을 지정할 수 있지만 여전히 다음 요소는 개행되어 나타난다.

`inline` 은 block 과 달리 줄 바꿈이 되지 않고, width와 height를 지정할 수 없다는게 그 특징이다. 대표적으로 `span` `b` `strong` `i` 태그가 있다.

`inline-block` 은 block과 inline의 중간 단계다. 즉, width와 height는 지정할 수 있지만 개행은 되지 않는 놈이다.

![img](https://media.vlpt.us/images/ljinsk3/post/23bb2fba-cdb2-4e7a-b008-6ccfedbae2f4/Screen%20Shot%202020-04-17%20at%206.57.41%20PM.png)

### flex

flexible-box를 사용할 수 있는 display 속성이다. 각각의 요소들을 item으로 보고 item들을 효과적을 정렬하고 배치할 수 있도록 도와주기 때문에 flex를 잘 이해하고 습득하신다면 아주 효과적인 웹 페이지를 만드실 수 있을 것이다.

flex는 두 가지 관점에서 볼 수 있는데 하나는 부모 역할을 하는 `container 입장`이고, 두 번째는 각각의 container 안에서 자식 역할을 하는 `item 입장` 이다.

![img](https://images.velog.io/images/ljinsk3/post/4f65703b-a87d-4af0-9966-c4e7e549dc9d/Screen%20Shot%202020-04-17%20at%207.09.55%20PM.png)![img](https://images.velog.io/images/ljinsk3/post/ecc47b54-4390-4490-be53-e2bba73fa3ec/Screen%20Shot%202020-04-17%20at%207.10.48%20PM.png)

먼저 container 입장에서 사용할 수 있는 속성을 하나씩 살펴보겠다.

#### container

#### 1. flex-direction

flex-direction은 안에 있는 Item들을 정렬할 때 어떤 순서로 정렬할 지, 가로로 정렬할지 세로로 정렬할지를 선택할 수 있다. 정방향 가로정렬이 기본값이다.
![img](https://images.velog.io/images/ljinsk3/post/38f9124a-f43f-4527-bf6c-8bfd3e6a9300/Screen%20Shot%202020-04-17%20at%207.01.27%20PM.png)

```css
.container {
  flex-direction: row | row-reverse | column | column-reverse;
}
```

#### 2. flex-wrap

flex 는 기본적으로 item을 한줄에 정렬하려고 한다. 이때 중간에 끊고 줄바꿈을 하고 싶다면 flex-wrap을 사용할 수 있다. no-wrap이 기본값이다.

![img](https://images.velog.io/images/ljinsk3/post/21392b53-9172-42b5-8df2-7cea714604b3/Screen%20Shot%202020-04-17%20at%207.16.17%20PM.png)

```css
.container {
  flex-wrap: nowrap | wrap | wrap-reverse;
}
```

#### 3. justify-content

메인 축을 중심으로 아이템들을 여백과 함께 정렬하는 방식을 지정할 수있다.
flex-start가 기본 값이며 중앙 정렬을 원할 경우 `center`나 `space-around`등을 많이 사용한다.

![img](https://images.velog.io/images/ljinsk3/post/619ad5b7-8a7c-4f94-9ece-f0800e04f3c8/Screen%20Shot%202020-04-17%20at%207.00.34%20PM.png)

```css
.container {  
  justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly | start | end | left | right ... + safe | unsafe; 
}
```

#### 4. align-content

flex-wrap 을 사용해서 item이 여러 줄로 존재하고 있을 때, 여백과 함께 정렬하는 방식을 지정할 수 있다. 기본값은 flex-start이며, 한 줄 밖에 없을 때는 justify-content와 똑같다.

![img](https://images.velog.io/images/ljinsk3/post/46cf82a5-76f8-4c5b-bed0-8cb2e9217151/Screen%20Shot%202020-04-17%20at%207.22.30%20PM.png)

#### 5. align-items

container 안에서 items 들간의 세로정렬을 하는데 쓰인다.

![img](https://images.velog.io/images/ljinsk3/post/4aeb3d9d-0a46-410e-8ca6-dedabe445771/Screen%20Shot%202020-04-17%20at%207.00.56%20PM.png)

```css
.container {
  align-items: stretch | flex-start | flex-end | center | baseline | first baseline | last baseline | start | end | self-start | self-end + ... safe | unsafe;
}
```

#### item

#### 1. order

각각의 아이템은 기본적으로 html 에 나열된 순서대로 우선순위가 매겨진다. 하지만 order를 임의로 지정하면 지정한 order 순서대로 정렬할 수 있다.

![img](https://images.velog.io/images/ljinsk3/post/bcde141c-2d18-4273-92df-5026beb65edf/Screen%20Shot%202020-04-17%20at%207.25.20%20PM.png)

##### 2. flex-grow

flex grow는 각 아이템들이 공간을 차지하는 비율을 지정한다. 기본 값은 모두 1이며 모두 1일 경우에는 공간이 균등하게 분배되지만 한 아이템이 2이면 해당 아이템에만 2배의 공간을 할당하고 나머지 공간을 남은 아이템들이 균등하게 가져간다.

기본값으로 `flex : 1`이렇게 만 적어도 된다.

![img](https://images.velog.io/images/ljinsk3/post/9b696d98-44d8-46fe-be76-a2a26b8ba309/Screen%20Shot%202020-04-17%20at%207.29.09%20PM.png)

[사진 출처 : flex-guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

[게임으로 Flex-box 연습하기!!](https://flexboxfroggy.com/#ko)

### align

[참고자료 : 여러가지 방법으로 정렬하기](https://wit.nts-corp.com/2017/02/06/4123)

1. **text-align**

   block 요소 안에 있는 inline 요소를 정렬 한다. 여기서 inline 요소란 `span`,`p`,` img` 등이 포함된다.

   정의는 block요소에 해야 한다. center, left, right, 등 사용 가능하다.

2. **margin**

   정렬하고하자하는 요소의 width가 지정되어있다면 `margin: 0 auto;` 를 사용해서 중앙 정렬이 가능하다.

   width 를 지정할 수 없는 inline 요소는 쓸 수 없다.

3. **flex**

   ```css
   .container {
     display: flex;
     justify-content: center;
   }
   ```

### float

요소를 띄우는 속성으로서 원래 웹페이지에서 **이미지**를 어떻게 띄워서 텍스트와 함께 배치할 것인가에 대한 속성이다.

![img](https://images.velog.io/images/ljinsk3/post/d278fc17-7b1a-4ff2-97f7-293662ed5d40/float.png)

또한 한 라인에 요소들을 각각 오른쪽과 왼쪽에 배치할 때도 유용하게 쓰일 수 있다.

float을 사용할 때 주의할 점은, 자식요소의 높이 값을 부모가 전혀 인식할 수 없다는 것이다. 이를 해결 하기 위해서 .clearfix라는 가상 선택자를 만들어서 부모 요소에 클래스를 추가해주면 된다. 의미없는 빈 엘리먼트를 사용하지 않으면서도 flaot을 클리어 할 수 있다.

`::after`란 가상 선택자로 css를 통해서 가상으로 요소를 만들어 낼 수 있다.

```css
.clearfix::after {
  content: "";
  clear: both;
  display: block;
}
```

### background

##### `background-image`, `background-color`, `background-size`, `background-position`, `background-repeat` ..등등이 있다.

```css
.container {
  background: url("test.jpg"); 
}
```





출처:https://velog.io/@ljinsk3/CSS-%EA%B8%B0%EC%B4%88-%EB%82%B4%EC%9A%A9-%EC%A0%95%EB%A6%AC