1. 바탕화면에 폴더 생성 및 VScode 터미널 실행

2. 가상환경 생성 및 활성화

   ```bash
   $ python -m venv venv
   
   $ source venv/Scripts/activate
   (venv)
   $ pip install django==3.2.12
   ```

3. 프로젝트 생성 : **`.` 잊지 말기**, 단수형으로

   ```bash
   $ django-admin startproject pjt .
   (venv) 
   ```

4. 서버 시작하기 : ctrl 누르고 서버링크 클릭하면 로켓 나온다. crtl+c 하면 빠져나옴

   ```bash
   $ python manage.py runserver
   ```

5. 앱 생성 : 복수형으로

   ```bash
   $ python manage.py startapp articles
   ```

6. 앱 등록 : settings.py 에서 변수명은 언더바로, 설치된 앱이라는 리스트에 추가

   > 반드시 앱 생성 후 등록! => 등록 후 생성하면 앱이 생성되지 않는다!!!!

   ```python
   INSTALL_APPS = [
       'articles',
       ..
   ]
   ```

   추가설정

   ```python
   # 이 설치의 언어 코드를 나타내는 문자열
   LANGUAGE_CODE = 'en-us' -> 'ko-kr'
   # 데이터베이스의 연결의 시간대를 나타내는 문자열 지정
   TIME_ZONE = 'UTC' -> 'Asia/Seoul'
   # 번역 시스템 활성화 여부
   USE_I18N = True
   # 지역화된 데이터 형식이 기본적으로 활성되는지 여부
   USE_L10N = True
   # datetimes가 기본적인 시간대인지 인식하는 여부,False 인 상태로 타임존 설정하면 에러
   USE_TZ = True
   ```

   

7. URLs : HTTP 요청을 적절한 view로 전달

   > urlpatterns 는 리스트로 되어있고, path 함수에는 ('index/', view.index)
   >
   > from articles import views 를 이용

   ```python
   from django.contrib import admin
   from django.urls import path
   from articles import views
   
   urlpatterns =[
       path('admin/', admin.site.urls),
       path('index/', views.index),
   ]
   ```

8. Views : HTTP 요청을 views에서 전달 받으면, 요청 수신 후 HTTP 응답을 반환하는 함수를 작성

   > DB가 있으면 models.py를 통해 요청에 맞는 데이터에 접근
   >
   > Template에게 HTTP 응답 서식을 맡겨

   ```python
   from django.shortcuts import render
   def index(request):
       return render(request, 'index.html')
   ```

9. Templates 생성 : 실제 내용을 보여주는데 사용되는 파일, 파일의 구조나 레이아웃을 정의

   > templates라는 폴더 안에서 index.html 파일이 있는 구조

- Template 파일 경로의 기본 값은 : app(articles) 폴더 안의 (templates) 폴더안에 저장되어 있다.

- DTL (Django Templates Langauge) : HTML에서 표현을 위해 사용되는 조건,필터,변수,태그 를 이용해 데이터를 표현하는 언어이다. python 코드가 실행되는 것이 아님!!!

  - variable : `{{ variable }}` : views.py에서 render()를 통해 변수를 template으로 받아야함.

    - 변수명은 밑줄 먼저로는 사용 불가

    -  `.`으로 변수 속성에 접근 가능

    - render의 세번째 인자로 {'key' : value}와 같이 딕셔너리 형태로 넘겨준다.

      key에 해당하는 문자열이 template에서 사용가능한 변수!!	

    ```python
    import random
    
    def greeting(request):
        foods = ['apple', 'banana', 'coconut']
    
        info = {
            'name' : '미애'
        }
        context = {
            'foods' : foods,
            'food' : random.choice(foods),
            'info' : info
        }
        return render(request, 'greeting.html', context)
    ```

    ```django
    <p>안녕하세요 변수에 접근하려고 .을 찍은 제이름은 {{ info.name }} 입니다.</p>
    <p>리스트에서 받아온 음식들은 {{ foods|join:"," }} 입니다</p>
    <p>첫번째 리스트 음식은 리스트에서 . 을찍고 인덱스를 찍어서{{foods.0}} </p>
    <p>랜덤으로 가져올 음식은 {{food|length}}입니다</p>
    <a href="/index/">뒤로</a>
    ```

    

  - filter : `{{ varible|filter}}` : 표시할 변수를 수정할 때 사용, 소문자나 30자 이내나 이런거

  - tags : `{% tags %}` 출력 텍스트나 반복, 논리 수행 등 제어 흐름을 만들 때 사용
    - {% if %} {%end if%} 혹은 {% for %} {% endfor %} 이런거 24개 있음

  - comments : `{# 라인주석 #}` `{% comment %} 문단 주석 {% endcomment %}`

10. 코드 작성 순서 : `urls.py  => views.py => template.html` 



11. 템플릿 상속

    templates 폴더 생성 => base.html 생성 

    ```django
    {#!+tap#}
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
       {#간단한 navbar#}
      <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Navbar</a>
      </nav>
      {% block content %}
      {% endblock content %}
    </body>
    </html>
    ```

    include : templates에서 nav 부분 따로 빼서 _nav.html 생성

    > _언더바는 단순히 include 되는 템플릿이라는 것을 분류하는 수단

    ```django
    {% include '_nav.html' %}
    ```

    

    12.  HTML Form

        urls.py

        ```python
            path('throw/', views.throw),
            path('catch/', views.catch)
        ```

        views.py

        ```python
        def throw(request):
            return render(request, 'throw.html')
        
        def catch(request):
            message = request.GET.get("message")
            context = {
                'message' : message,
            }
            return render(request, 'catch.html', context)
        ```

        throw.html

        ```django
        <form action="/catch/" method="GET">
            <label for="message">라벨 포</label>
            <input type="text" id="message" name="message">
            <input type="submit">
        </form>
        ```

        catch.html

        ```django
        <p1>{{message}}</p1>
        ```

        

13. URL variable routing

    > URL 주소를 변수처럼 사용하여 path()에 여러 페이지를 연결시킬 수 있음!!!

    ```python
    path('<int:number>/',views.example)
    ```

    

14. App mapping을 통해 urls를 각 app에서 관리할 수 있도록 한다.

    name도 붙일 수 있다.