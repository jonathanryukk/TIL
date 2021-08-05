#### ** 줄바꿈 태그 : <br>**

<br>은 시작태그이면서 종료태그의 형태를 취한다.

```
<br	/>
```

 

원래는 위와 같이 슬러시를 표시해주어야 하지만, HTML5로 넘어오면서 슬래시를 표현하지 않아도 오류가 나지 않게 되었다. 따라서 그냥 <br>로만 표기해도 된다.

 

 

#### **공백문자 : **

공백 또는 여러 특수문자를 사용해야 하는 경우, HTML에서는 앞에 &, 뒤에 ;를 붙여 표현한다.

그 중에서 &nbsp;는 공백을 표현하는 문자이다.

 

 

#### **단락 표현 : <p></p>**

 

기본적으로 block 태그이다.

그러나 그 안의 요소들은 원래 본인의 속성대로(block or inline) 적용된다.

 

<div>와 <p>의 차이는 p는 문자 단락 용도이고, div는 레이아웃 계층 나누기 용도라는 점이 다르다.

 

<div></div> : 아래 단락과 붙어서 표현됨

<p></p> : 아래 단락과 떨어져서 표현됨

 

\>>> margin 속성으로 제어 가능

 

 

#### **선그리기 : <hr>**

hr도 기본적으로 block tag이다.

속성으로는 width / color / size(두께) 가 있다.

아무것도 설정하지 않을 시 연회색 선이 block으로 그어져 표현된다.

size는 1부터 표현

```
<hr width = "200px">
```

이런 식으로 선의 길이를 조절할 수 있음.

이 때, 자동으로 가운데 정렬되어 출력

 

```
<hr width = "30%">
```

위와같이 px이 아닌 %로 표현시 브라우저 창의 크기에 맞춰 길이가 조절된다.

 

 

#### **타이틀 : <h></h>**

기본적으로 block 태그이다.

h는 header라는 뜻을 나타낸다.

속성으로 align을 가진다.(정렬)

 

1~6까지 사이즈를 가질 수 있으며, 1이 가장 크고 6으로 갈수록 커진다.

<div style = "font-weight: bold;> 라고 된 것과 같은 효과이다.

 

```
<h1 align="right"> 타이틀 </h>
<h1 align="center"> 타이틀 </h>
```

h 태그는 디폴트가 왼쪽정렬인데,

align 속성에 right, center를 값으로 주어 정렬방식을 변경할 수 있다.

 

 

#### **자주쓰는 특수문자들 : < > &**

```
	&lt;  <!-- < 문자: lt stands for less than -->
	&gt;  <!-- > 문자: gt stands for greater than -->
	&amp; <!-- & 문자: am percent-->
```

 

 

#### **입력한 형식 그대로 보여주는 태그 : <pre></pre>**

엔터, 공백, 탭 등의 형식을 입력한 대로 보여주는 

 

 

#### **인용부분을 나타내는 태그 : <q></q>**

```
문장 안에서 어떤 것을 인용했다고 표현하고 싶을 때, <q>이렇게</q> 표현할 수 있다.
```

인라인 태그로서, 양쪽에 쌍따옴표를 표현해줄 수 있다.

 

 

#### **인용단락을 나타내는 태그 : <blockquote></blockquote>**

```
<blockquote>
단락 기준으로 인용구문을 적어주고 싶을 때는 이렇게 표현한다.
</blockquote>
```

속성으로 cite = "인용해 온 곳 url" 을 표현 가능

cite 속성은 출처에 대한 기록일 뿐, 해당 링크로 이동시켜주진 않는다.

 

 

 

#### **이미지 파일 : <img>**

**속성들**

src = "이미지 경로"

alt = "이미지가 표시되지 않을 시 대체하여 표시할 텍스트"

width = "가로너비"

height = "세로높이"

border = "테두리너비(1부터)"

style = "border-color: 테두리 색깔"

title = "마우스오버 시에 표시할 텍스트"

 

이미지 경로는 절대경로 또는 상대경로로 표현할 수 있다.

아래글 참고 >>

[ [JavaWeb\] 파일경로 - 절대경로, 상대경로/프로젝트명/WEB-Content/ ./ 현재폴더 밑에 있는codingwanee.tistory.com](https://codingwanee.tistory.com/entry/JavaWeb-파일경로-절대경로-상대경로)

 

#### **이미지를 관리하는 태그 : <figure><figcaption>**

```
<figure>
	<img src="경로">
	<figcaption>
	사진 아래 표시될 설명
	</figcaption>
</figure>
```

시멘틱 태그(문서 내 구문적 정보를 보여주는 태그)로서,

특히 사진이나 일러스트 등을 표현하는 데 사용한다.

 

 

#### **선택 가능한 옵션을 보여주는 태그 : <select><optgroup><option>**

 



![img](https://blog.kakaocdn.net/dn/bn0prm/btqEKRj8nOy/cfeQKL3uJDyyUGWQV9G020/img.png)



```
	<select multiple>
    	<optgroup label="옵션분류1">
		<option>옵션1</option>
		<option>옵션2</option>
		<option selected="selected">옵션3</option>
        </optgroup>
      	<optgroup label="옵션분류1">
		<option>옵션1</option>
		<option>옵션2</option>
        </optgroup>
	</select>
```

 

**select 속성**

multiple = "multiple" : ctrl 키를 누를 경우 여러개의 옵션 선택 가능

 

**optgroup 속성**

label = "옵션분류"

 

**selected 속성**

selected = "selected" : 속성이 적용된 옵션이 가장 상위에 표기됨

 

이렇게 속성명="속성값"인 경우, 속성명만 표기해도 된다.

 

 

#### **선택-옵션 업그레이드 된 버전 : <datalist></datalist>**

```
	<input list="리스트">
	<datalist id="카테고리">
		<option> 옵션1 </option>
		<option> 옵션2 </option>
		<option> 옵션3 </option>
	</datalist>
```



출처:https://codingwanee.tistory.com/entry/JavaWeb-%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%EC%9E%90%EC%A3%BC%EC%93%B0%EB%8A%94-%EC%9C%A0%EC%9A%A9%ED%95%9C-HTML-%ED%83%9C%EA%B7%B8%EB%93%A4