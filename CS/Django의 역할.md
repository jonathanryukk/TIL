[[개념\] Django는 Web Server가 아니라구요!!](https://jay-ji.tistory.com/66)

[💻 프로그래밍/Django](https://jay-ji.tistory.com/category/💻 프로그래밍/Django) 2020. 8. 10. 19:38



안녕하세요! **운동하는 개발자 Jay**입니다. 오늘은 **Django, Nginx, WSGI,** **gunicorn**의 개념적인 내용을 간단히 다뤄보려고 합니다.
사실 웹 개발자로서 처음 커리어를 시작했을때, 많이 헷갈렸던 부분이었습니다.

 

> **"우리 회사 웹 서버는 Django를 사용해!"** 

 

개발자 친구들을 만나면 이렇게 설명 했던 것 같습니다.ㅎㅎㅎ 근데 사실 **정확히 따지자면, 틀린 말이죠!** (창피함😱)

아마, 저 처럼 처음 웹 개발자로서 커리어를 시작하시는 분들도 이런 개념에 헷갈리셨을 수도 있을 것 같아요! (**나만 그런 건가 hoxy?**)

 

## **1. Django의 역할이 그래서 정확히 뭔데??**

------



![img](https://blog.kakaocdn.net/dn/kU3nw/btqGnINfMg2/5Kqk8CbWeXUknlbI5k4roK/img.png)



네! 그래서 **Django**의 역할은 도대체 뭘까요? 이미 다들 알고 계신텐데 **Django**는 **Web Server**가 아니라 **Web Application Framework**입니다. 

 



![img](https://blog.kakaocdn.net/dn/bcnhKq/btqGrjez1Lc/vfEfFzOtKygk5lqSHa0Hm0/img.png)Django 설명



보통 처음 **Django** 듀토리얼을 시작하게 되면, 프로젝트를 생성하고 아래 명령어로 서버를 실행합니다.

 

> ./manage.py runserver (= python manage.py runserver)

 

하지만, 이것은 **debug**용으로 **local**에서만 사용해야 하고 실제 **production** 환경에서는 추천하지 않습니다.(사용 x)

 



![img](https://blog.kakaocdn.net/dn/PiUeS/btqGqQwUV0B/qjZCFwNVpWBM92ySs2Oga1/img.png)Django runserver 설명중 일부분



**Django** 공식 문서에서도 **production setting에서 사용하지 말라**고 주의를 주고 있습니다. (보안 및 퍼포먼스 이슈 있을 수 있음)

그리고 두번째 줄에 보면 **Django**는 **Web server**가 아니라고 말합니다.

 

정확히는 Django 개발자가 ***"우리는 웹 프레임워크를 만들지 웹 서버를 만드는 건 아닌다. 그래서 실서버 환경에서 다룰 수\* \*있는 건 Django의 영역 밖이다."\*** 라고 말하고 있네요. ㅎㅎ 그래서 요약하자면,

> Django는 Web Server 가 아니라 Web Framework이다!

 

 

## **2. 그래서 Web Server는 뭐야?**

------

자, 이번 글의 핵심중 하나죠! **Web Server**!! 두구두구두구.....

(대문작 만하게 이미지를 넣어놓고 두구두구 하는 당신은...대체...🤔)



![img](https://blog.kakaocdn.net/dn/bfMs3s/btqGqb2uok6/ZCLpZ6hFSl2imZazNJHedk/img.png)



> Web Server는 Nginx, Apache 같은 소프트웨어를 말합니다!

짜란!! 사실 저는 **Nginx**를 단순히 **proxy**(프록시) 기능을 하는 소프트웨어(?) 정도로만 생각했습니다.

이것도 **Nginx**의 기능이고 맞는 말이지만, 적어도 설명을 할 때 ***"Django를 Web Server로 사용하고 있어"***라는 말 하는 게 아닌 ***"Web Server는 Nginx고 Server Side Framework는 Django를 사용하고 있어!"*** 라고 말해야 할 것 같습니다.

 

#### 📌 **Web Server의 역할** 

웹 서버의 주된 기능은 웹 페이지를 [클라이언트](https://ko.wikipedia.org/wiki/클라이언트)로 전달하는 것이다. 주로 [그림](https://ko.wikipedia.org/wiki/그림), [CSS](https://ko.wikipedia.org/wiki/CSS), [자바스크립트](https://ko.wikipedia.org/wiki/자바스크립트)를 포함한 [HTML](https://ko.wikipedia.org/wiki/HTML) 문서가 [클라이언트](https://ko.wikipedia.org/wiki/클라이언트)로 전달된다. (from [위키백과](https://ko.wikipedia.org/wiki/웹_서버))

 

위키에도 나와있듯이 웹서버는 **정적(image, css, js)인 정보**를 반환하는 역할을 합니다. 대표적인 **Web Server**로는 **Nginx, Apache, GWS** 등이 있죠!

 

개인적으로 **Apache**는 대학교 2학년 때 (어언 7년...) 토이 프로젝트 한다고 써봤고, 지금 다니는 회사에서 웹 개발자로 일하면서 **Nginx**를 써봤네요ㅎㅎ 요즘에는 **Nginx**를 많이 쓴다고 합니다.

 

**Apache**와 **Nginx**의 차이는 간단하게 **Apache**는 **request**에 대해 **process**(+thread) 하나씩 사용하고 **Nginx**는 **Event-Driven** 방식으로 비동기 처리한다고 합니다. 두 Web Server의 차이는 [여기서](https://taes-k.github.io/2019/03/08/server-nginx-event-driven/) 확인해 주세요!

 

 

## **3. WSGI는 또 뭐고 gunicorn은 뭐야?**

------

**WSGI**는 **Web Server Gateway Interface**의 약자입니다. **WSGI**는 **python application**(python script)이 **Web Server**와 통신하기 위한 **표준 Interface**이며 **Python Framework**입니다! (일종의 프로토콜이라고 생각하면 쉬울 것 같아요)

 

#### 📌 **WSGI 간단 설명** (from [위키백과](https://ko.wikipedia.org/wiki/웹_서버_게이트웨이_인터페이스))

WSGI는 [서버](https://ko.wikipedia.org/wiki/서버)와 [게이트웨이](https://ko.wikipedia.org/wiki/게이트웨이) , [애플리케이션](https://ko.wikipedia.org/wiki/애플리케이션)과 [프레임워크](https://ko.wikipedia.org/wiki/프레임워크) 양단으로 나눠져 있다. WSGI 리퀘스트를 처리하려면, 서버단에서 환경정보와 콜백 함수를 애플리케이션단에 제공해야 한다. 애플리케이션은 그 요청을 처리하고 미리 제공된 콜백 함수를 통해 서버단에 응답한다. WSGI 미들웨어(라고 불린다.)가 WSGI 서버와 애플리케이션 사이를 보충해주는데, 이 미들웨어는 서버의 관점에서는 애플리케이션으로, 애플리케이션의 관점에서는 서버로 행동한다. 이 미들웨어는 다음과 같은 기능을 가진다.

- 환경변수가 바뀌면 타겟 URL에 따라서 리퀘스트의 경로를 지정해준다.
- 같은 프로세스에서 여러 애플리케이션과 프레임워크가 실행되게 한다.
- XSLT 스타일시트를 적용하는 것과 같이 전처리를 한다.

 

> **HTTP requests** -> **Web Server** -> **WSGI Server**(Middleware) -> **Django**(WSGI를 지원하는 Web Application)

 

이런 식으로 동작이 이루어진다고 볼 수 있습니다. 여기서 **WSGI Server**라고 있죠? 바로 이것이 **gunicorn**입니다.

(이 외에도 mod_wsgi, uwsgi 등이 있음)

 

#### **📌 gunicorn 간단 설명** 



![img](https://blog.kakaocdn.net/dn/kVZ3t/btqGte4ZoG8/vuozP4Nxe79z8nqZyDgpmk/img.png)gunicorn(green unicorn)



**gunicorn**은 **Python WSGI HTTP Server**입니다. **gunicorn**은 상대적으로 빠르고 가볍고 사용이 쉽다고 합니다.

특징은 이렇습니다.

- [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), [web2py](https://en.wikipedia.org/wiki/Web2py), [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) 그리고 [Paster](https://en.wikipedia.org/wiki/Python_Paste) 를 지원
- Automatic worker [process management](https://en.wikipedia.org/wiki/Process_management_(computing))
- 간단한 Python configuration
- Multiple worker configurations
- 확장성(extensibility)을 위한 다양한 Server hook들
- python2.6+ 그리고 python3.2+ 과 호환 가능

 

**Django**에서는 **wsgi.py**에서 **application = get_wsgi_application()** 를 통해 **wsgi handler**를 가져옵니다. **wsgi handler**에서는 **middleware**등 을 처리하고, **WSGI server**에서는 설정을 읽어 **application**의 경로를 가져옵니다.

**Django** 기본 명령어인 [runserver](https://docs.djangoproject.com/en/3.0/ref/django-admin/#runserver) 명령은 [WSGI_APPLICATION](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-WSGI_APPLICATION) 설정에서 경로를 가져옵니다. 



 

## **4. 마치며(요약)**

------



![img](https://blog.kakaocdn.net/dn/Q00Ay/btqGuqjD4JU/kvM3Jgdu77dBHqi6sqkfh1/img.png)Nginx, WSGI Server(gunicorn), Django 관계



그래서 위 내용들을 그림으로 보기 쉽게 요약하면, 위 이미지처럼 볼 수 있습니다!! (그림으로 보니까 한눈에 보이죠?!)

이런 용어들이나 관계에 대한 개념에 대해서 아는 것은 ***다른 개발자들과 커뮤니케이션할 때 정말 중요***한 것 같습니다. 그리고 개념이 정확히 잡혀야 처음부터 프로젝트를 만들 때 어느 정도 프로젝트 전체적인 아키텍처도 보이고요!

 

저도 아직 잘 몰라 정리해보려고 만들어서 설명이 많이 부족하지만, 다른 분들에게 조금이나마 도움이 되었으면 좋겠네요!

그럼 오늘 하루도 즐거운 하루 보내세요!!

(잘못된 설명이 되어있는 부분이 있다면, 댓글로 알려주시면 많은 도움이 될 것 같습니다!!🙏)