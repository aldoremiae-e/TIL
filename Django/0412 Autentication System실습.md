# 0412 실습

> 참고문헌 : https://docs.djangoproject.com/en/4.0/topics/auth/default/#

## accounts App 생성

1. 가상환경 실행
2. `pip install -r requirements.txt`
3. `python manage.py startapp accounts`
4. `settings.py` 에 `INSTALLS_APPS` 에 앱 추가
5. `pjt\urls.py` 에  `path('accounts/', include('accounts.urls')),`



## 로그인

- AuthoenticationForm : 사용자 로그인을 위한 form, request를 첫번째 인자로 취함

- from django.contrib.auth. import login as auth_login 안에 있는 get_user() 메서드
  - 유효성검사가 통과되면 사용자 객체 할당, 아니면 None
- 

## 회원가입

> accounts 앱에서 urls => views => templates/acoounts

- urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    
]
```



- views.py
  - (1) => (2) => (3) 순으로 생각하고 작성하기.

```python
from django.shortcuts import redirect, render
# Built in form을 사용하고 있기 때문에 forms.py 생성하지 않음
from django.contrib.auth.forms import UserCreationForm # 회원가입 모델폼
from django.views.decorators.http import require_http_methods
```

```python
@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':    
        # (3) form 작성
        form = UserCreationForm(request.POST)
        if form.is_valid(): # 유효성검사
            form.save() # 저장
            return redirect('articles:index')
    else : # (2) GET 먼저
        form = UserCreationForm()   # 빈 form 생성
    # (1) 내용
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```



- signup.html

```django
{% extends 'base.html' %}

{% block body %}
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method='POST'>
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Submit">
</form>
<a href="{% url 'articles:index' %}">BACK</a>
{% endblock body %}
```

부트스트랩 이용 = >

```django
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block body %}
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method='POST'>
  {% csrf_token %}
  {% bootstrap_form form %}
  <input type="submit" value="Submit">
</form>
<a href="{% url 'articles:index' %}">BACK</a>
{% endblock body %}

```



- db.sqlite3 => auth_user
- 
  - last_login : NULL이 허용이 되어있다
  - is_superuser : 1 / 0 부울형
  - is_staff : 1 / 0 부울형
  - is_activate : 활성화상태 (휴면계정)
  - date_jouned : 가입
  - password : 암호화되서 저장됨

<img src="0412%20Autentication%20System%EC%8B%A4%EC%8A%B5.assets/image-20220412102014508.png" alt="image-20220412102014508" style="zoom:150%;" />

![image-20220412102028843](0412%20Autentication%20System%EC%8B%A4%EC%8A%B5.assets/image-20220412102028843.png)



- Shell_plus에서

  - user을 article처럼 .create를 이용해서 db를 만들면 안됨

    - 이유 : password 가 **암호화** 되지 못함

    - 해결방법 https://docs.djangoproject.com/en/4.0/topics/auth/default/#creating-users

      ![image-20220412103707751](0412%20Autentication%20System%EC%8B%A4%EC%8A%B5.assets/image-20220412103707751.png)

    - <img src="0412%20Autentication%20System%EC%8B%A4%EC%8A%B5.assets/image-20220412104423435.png" alt="image-20220412104423435" style="zoom:50%;" />	



<hr>

## 로그인 - 로그아웃

AuthenticationForm : 모델폼이 아닌 그냥폼

로그인(서버 : 세션정보) = > 사용자 브라우저 쿠키 (request 객체를 활용할 것)

GET(form) POST(로직)

