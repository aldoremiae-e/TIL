# 🤓0420 REST API

[TOC]

## 🌞HTTP

> HyperText Transfer Protocol

- 웹에서 이루어지는 모든 데이터 교환의 기초
  - 요청 (request) : 클라이언트의 요청에 의해 전송되는 메세지
  - 응답 (response) :  서버에서 응답으로 전송되는 메세지

- Stateless 하고 Connectionless 하므로 **쿠키와 세션** 을 통해 서버 상태를 요청과 연결

- HTTP request methods

  > 리소스(HTTP 요청대상)에 대한 행위를 정의

  - GET(가져오기), POST(요청받기), PUT(쓰기), DELETE(지우기)

- URI (Uniform Resource Identifier): 통합 자원 식별자

  - URL (Uniform Resource Locator) :통합 자원 위치 (웹주소, 링크)

  - URN (Uniform Resource Name) : 통합 자원 이름 (ISBN - 국제표준도서번호)

    <br>

  - URI 구조

    1. Schema 스키마 : 브라우저가 사용해야하는 프로토콜	 (https://)

    2. Host 호스트 : 요청을 받는 웹 서버의 이름 	(www.example.com)

    3. Port 포트 : 웹 서버 상의 리소스를 접근하는데 사용되는 게이트
       - HTTP 표준 포트 : HTTP 80, HTTPS 443

    4. Path 패스 : 웹 서버 상의 리소스 경로 	(/path/to/myfile.html)

    5. Query 쿼리 : 웹 서버에 제공되는 추가적인 매개 변수 (/?key=value)
    6. Fragment : 리소스 안에서 북마크의 한 종류, 부분 식별자라고 부르며, # 뒤부분은 요청이 서버에 보내지지 않음 (#quick-start)



## 🌞RESTful API

### 	⭐API

> Application Programming Interface 

- 앱을 프로그래밍 언어가 제공하는 기능으로 수행할 수 있게 만든 인터페이스

- 응답 데이터 타입 : HTML, XML, JSON

### 	⭐REST

> REpresentational State Transfer

- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - 네트워크 구조원리의 모음
  - 자원을 정의하는 방법에 대한 고민필요

- REST의 자원과 주소 지정 방법
  - 자원 : URI
  - 행위 : HTTP Method
  - 표현 : 자원과 행위를 통해 궁극적으로 표현되는 결과물, JSON으로 표현된 데이터를 제공

- JSON (JavaScript Object Notation) : 문자열

  - 사람이 읽거나 쓰기 쉽게 계기가 파싱하고 만들어내기 쉬움

  - 파이썬 딕셔너리, 자바스크립트 오브젝트처럼, C계열의 언어가 갖고있는 자료구조로

    쉽게 변화할 수 있는 key-value 형태의 구조를 가짐

- **정보**는 **URI**로 표현, **행위**는 **HTTP Method**로 표현



## 🌞Response

> urls.py

```python
# my_api.urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```

```python
# articles.urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
]
```



> views.py

- **return 값 **: `JsonResponse` objects

  - JSON-encoded response 만드는 HttpResponse 의 서버 클래스

    ```python
    return JsonResponse(articles_json, safe=False)
    ```

    직렬화 : 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하거나 나중에 재구성할 수 있는 포맷으로 변환하는 과정

- **return 값 ** : `HttpResponse`

  - ```python
    return HttpResponse(data, content_type='application/json')
    ```

- **return 값** : `Django rest_framework`(DRF)

  1. **ModelSerialize** : Article 모델에 맞춰 자동으로 필드를 생성해 serialize 해줌

     ```python
     # articles/serializers.py
     from rest_framework import serializers
     from .models import Article
     
     
     class ArticleSerializer(serializers.ModelSerializer):
     
         class Meta:
             model = Article
             fields = '__all__'
     ```

     ```python
     # articles/views.py
     from rest_famework.decorators import api_view
     from rest_framework.response import Response
     from .serializers import ArticleSerializer
     
     @api_view()
     def article_json_3(request):
         articles = Article.objects.all()
         serializer = ArticleSerializer(articles, many=True)
         return Response(serializer.data)
     ```

### 	⭐DRF

|              | Django ModelForm | DRF (Django REST Framework) |
| ------------ | ---------------- | --------------------------- |
| **Response** | HTML             | JSON                        |
| **Model**    | ModelForm        | Serializer                  |

- Web API 구축을 위한 Toolkit 을 제공하는 라이브러리

  > Web API : 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

- ModelForm과 매우 유사한 역할



## 🔥DRF를 이용한 Single Model 실습

1. 가상환경 및 패키지 설치

2. 프로젝트 생성

3. 앱 생성 및 등록

4. url 확인

5. 모델 생성 + makemigrations , migrate

   ```python
   from django.db import models
   class Article(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   ![image-20220424165248675](0420%20REST%20API.assets/image-20220424165248675.png)

   - dummy data 생성

     ```bash
     $ python manage.py seed articles --number=5
     Unknown command: 'seed' #에러
     ```

     에러 :  seed 가 없음

     ```bash
     $ pip install django_seed
     ```

     같은 에러 : 앱 등록 안되어있음

     ```python
     # Application definition
     
     INSTALLED_APPS = [
         'articles',
         'django_seed',
     ```

     에러 : `ModuleNotFoundError: No module named 'psycopg2'`

     ```bash
     $ pip install psycopg2
     ```

     해결

     ```bash
     $ python manage.py seed articles  --number=5
     {'verbosity': 1, 'settings': None, 'pythonpath': None, 'traceback': False, 'no_color': False, 'force_color': False, 'skip_checks': False, 'number': 5, 'seeder': None}
     Seeding 5 Articles
     Model Article generated record with primary key 1
     Model Article generated record with primary key 2
     Model Article generated record with primary key 3
     Model Article generated record with primary key 4
     Model Article generated record with primary key 5
     ```



5. serializers.py 생성

   ![image-20220424201827322](0420%20REST%20API.assets/image-20220424201827322.png)
   
   - 해결 : field가 아니라 fields



6. urls.py 

   1. 전체게시글목록
   2. 개별게시글은 `/<int:article_pk>/`필요

   

7. views.py 