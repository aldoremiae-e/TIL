# 0411 Authentication System

> 인증시스템



## 1. Authentication System

장고 인증 시스템은 django.contrib.auth 에 django contrib module로 제공

- django.contrib.auth : 인증 프레임워크의 핵심과 기본 모델을 포함
- django.contrib.contenttypes : 사용자가 생성한 모델과 권한을 연결할 수 있음



장고 인증 시스템은 인증과 권한부여를 함께 제공하며, 이러한 기능이 어느 정도 결합되어 일반적으로 인증 시스템이다.

- 인증 : 신원확인, 사용자가 자신이 누구인지 확인
- 권한 : 권한부여, 인증된 사용자가 수행할 수 있는 작업을 결정



## 2. 앱 생성하기

articles 과 같이 accounts 앱 생성

반드시 생성 후 등록!



## 3. 쿠키와 세션

>  로그인 로그아웃을 위해 필요한 개념

### 개념복습

- HTTP : HTML문서와 같은 리소스(데이터)들을 가져올 수 있는 프로토콜
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - 클라이언트 : 서버 프로토콜

  
  
- HTTP의 특징

  - 비연결지향(connectionless) : 서버는 **요청**에 대한 **응답**을 보낸 후 **연결을 끊음**
  
  - 무상태(stateless) : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝남
    - 상태 정보 유지X (로그인이 유지 되지 않음)
    - 클라이언트 - 서버가 주고 받는 메세지들은 서로 완전히 독립적임
    
    
  
  **클라이언트와 서버의 지속적인 관계를 유지하기 위해 (HTTP의 특징을 보완하기 위해) 쿠키와 세션이 존재**



### 쿠키

- 쿠키 : 서버가 서용자의 웹 브라우저에 전송하는 작은 데이터 조각

  - 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치(placed-on)되는 작은 기록 정보 파일

  - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장

  - 왜? HTTP는 상태가 유지되지 않기 때문에

    서버에 요청할 때 쿠키와 함께 전송하면서 HTTP의 상태가 유지되는 것 처럼 보이는 것이다.

    대표적 예 ) 로그인 상태 유지

    

- 쿠키의 사용 목적

  1. 세션 관리 (Session management)

     - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리

       ex) 쿠키를 삭제하면 그 정보가 싹 다 사라짐

  2. 개인화 (Personalization)
     - 사용자 선호, 테마 등의 설정
  3. 트래킹 (Tracking)
     - 사용자 행동을 기록 및 분석 - Secret browser





### 세션

- 세션 : 사이트와 특정 브라우저 사이의 **상태**를 유지시키는 것

  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 발급 받은 session id를 쿠키에 저장

    - 로그아웃 : 세션 삭제

    

- 쿠키 수명 : 쿠키의 수명은 두가지 방법으로 정의할 수 있음

  1. Session cookies : 현재 세션이 종료되면 삭제, 브라우저가 현재 세션이 종료되는 시기를 정의
  2. Persistend cookies : 지정된 날짜 똑은 속성에 지정된 기간이 지나면 삭제

  

- Session in Django

  - Django의 세션은 미들웨어를 통해 구현

    >  *미들웨어 : HTTP 요청과 응답 처리 중간에서 작동하는 시스템* 
    >
    > *HTTP요청 => 미들웨어=> URL-view-templates => 미들웨어 => HTTP응답*

    - SessionMiddleware : 요청 전반에 걸쳐 세션을 관리
    - AuthenticationMiddelsware : 세션을 사용하여 사용자를 요청과 연결

  - Django의 저장방식은 DB에 기본적으로 저장하는 것

  - sessio-id를 포함하는 쿠키를 사용해서 각각의 브라우저 사이에 연결된 세션을 알아냄

    - 세션 정보는 Django DB의 django-session 테이블에 저장



## 4. 로그인

> session을 Create 하는 로직과 같다
>
> Django에서 제공하는 built-in forms 을 활용



#### AuthenticationForm : 로그인 진행을 위한 사전 인증절차

- 사용자 로그인을 위한 form, request를 첫번째 인자로 취함

https://docs.djangoproject.com/en/4.0/topics/auth/default/#auth-admin

![image-20220413200710055](0411%20Authentication%20System.assets/image-20220413200710055.png)

```python
# views.py
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        # 데이터를 받아와서 => 아이디/비밀번호 일치 => 로그인(세션 생성) => redirect
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)
```

- `AuthenticationForm(request, request.POST)`<=> `ArticleForm(request.POST)` 와의 차이

​		: 받는 인자가 다르다 => `ArticleForm(request.POST)`은 ModelForm의 상속을 받는다.

​					`AuthenticationForm(request, request.POST)` 은 Form의 상속을 받는다.



​	**로그인은 세션을 만드는 과정이고, 회원가입은 DB에 저장이 되는 과정이므로 필요한 클래스가 다르다.**



#### login 함수

- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 (AuthenticationForm 유효성 검증을 통과한 경우)

  https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.login

  ![image-20220413203452602](0411%20Authentication%20System.assets/image-20220413203452602.png)

```python
# views.py
# 함수이름과 import하는 함수이름이 일치하면 안됨
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        # 데이터를 받아와서 => 아이디/비밀번호 일치 => 로그인(세션 생성) => redirect
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context) 
```



#### logout 함수

> session을 Delete하는 로직과 같음

현재 요청에 대한 session data를 DB에서 완전히 삭제하고, 클라이언트의 쿠키에서도 session-id가 삭제

- 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지

```python
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
```

```django
{% comment "로그아웃" %}{% endcomment %}
<form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <button class="btn btn-primary" type="submit">로그아웃</button>
</form>
```



#### 로그인 사용자에 대한 접근 제한

- 로그인 사용자에 대한 엑세스 제한 2가지 방법

  1. is_authenticated attribute 속성

     - User_model의 속성 중 하나

     - 모든 User 인스턴스에 대한 항상 True의 읽기 전용 속성 (AnonymousUser에 대해서는 항상 False)

       - 인증된 사용자인가 아닌가만 확인하는 용도

         권한과는 관련이 없다.

     ```django
     {% if request.user.is_authenticated %} 
           <form action="{% url 'accounts:logout' %}" method="POST">
             {% csrf_token %}
             <button class="btn btn-primary" type="submit">로그아웃</button>
           </form>
         {% else %}
           <a href="{% url 'accounts:signup' %}">회원가입</a>
           <a href="{% url 'accounts:login' %}">로그인</a>
     {% endif %}
     ```

     - `reqest.user` : 자주쓰이는 request 객체를 setting에 저장

       ![image-20220413210627891](0411%20Authentication%20System.assets/image-20220413210627891.png)



```python
# views.py 인증된 사용자인 경우 로그인 페이지에 들어가지 못하게하고, 로그아웃 페이지는 들어갈 수 있도록

def login(request):
    if request.uesr.is_authenticated:
        return redirect('articles:index')
    # ...
    
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')

```



2. login_required decorator

   - 사용자가 로그인되어 있지 않으면 settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect함
     - LOGIN_URL의 기본값 `/accounts/login/` <= app이름을 accounts로 한 이유

   ```python
   ## articles/view.py
   from django.contrib.auth.decorators import login_required
   
   @login_required
   def create(request):
       
   @login_required
   def update(request,pk):
   
   @login_required
   def delete(request,pk):
   ```

   - 인증 성공 시 사용자가 redirect되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨

   ![image-20220413211936173](0411%20Authentication%20System.assets/image-20220413211936173.png)