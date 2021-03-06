# ๐ค0420 REST API

[TOC]

## ๐HTTP

> HyperText Transfer Protocol

- ์น์์ ์ด๋ฃจ์ด์ง๋ ๋ชจ๋  ๋ฐ์ดํฐ ๊ตํ์ ๊ธฐ์ด
  - ์์ฒญ (request) : ํด๋ผ์ด์ธํธ์ ์์ฒญ์ ์ํด ์ ์ก๋๋ ๋ฉ์ธ์ง
  - ์๋ต (response) :  ์๋ฒ์์ ์๋ต์ผ๋ก ์ ์ก๋๋ ๋ฉ์ธ์ง

- Stateless ํ๊ณ  Connectionless ํ๋ฏ๋ก **์ฟ ํค์ ์ธ์** ์ ํตํด ์๋ฒ ์ํ๋ฅผ ์์ฒญ๊ณผ ์ฐ๊ฒฐ

- HTTP request methods

  > ๋ฆฌ์์ค(HTTP ์์ฒญ๋์)์ ๋ํ ํ์๋ฅผ ์ ์

  - GET(๊ฐ์ ธ์ค๊ธฐ), POST(์์ฒญ๋ฐ๊ธฐ), PUT(์ฐ๊ธฐ), DELETE(์ง์ฐ๊ธฐ)

- URI (Uniform Resource Identifier): ํตํฉ ์์ ์๋ณ์

  - URL (Uniform Resource Locator) :ํตํฉ ์์ ์์น (์น์ฃผ์, ๋งํฌ)

  - URN (Uniform Resource Name) : ํตํฉ ์์ ์ด๋ฆ (ISBN - ๊ตญ์ ํ์ค๋์๋ฒํธ)

    <br>

  - URI ๊ตฌ์กฐ

    1. Schema ์คํค๋ง : ๋ธ๋ผ์ฐ์ ๊ฐ ์ฌ์ฉํด์ผํ๋ ํ๋กํ ์ฝ	 (https://)

    2. Host ํธ์คํธ : ์์ฒญ์ ๋ฐ๋ ์น ์๋ฒ์ ์ด๋ฆ 	(www.example.com)

    3. Port ํฌํธ : ์น ์๋ฒ ์์ ๋ฆฌ์์ค๋ฅผ ์ ๊ทผํ๋๋ฐ ์ฌ์ฉ๋๋ ๊ฒ์ดํธ
       - HTTP ํ์ค ํฌํธ : HTTP 80, HTTPS 443

    4. Path ํจ์ค : ์น ์๋ฒ ์์ ๋ฆฌ์์ค ๊ฒฝ๋ก 	(/path/to/myfile.html)

    5. Query ์ฟผ๋ฆฌ : ์น ์๋ฒ์ ์ ๊ณต๋๋ ์ถ๊ฐ์ ์ธ ๋งค๊ฐ ๋ณ์ (/?key=value)
    6. Fragment : ๋ฆฌ์์ค ์์์ ๋ถ๋งํฌ์ ํ ์ข๋ฅ, ๋ถ๋ถ ์๋ณ์๋ผ๊ณ  ๋ถ๋ฅด๋ฉฐ, # ๋ค๋ถ๋ถ์ ์์ฒญ์ด ์๋ฒ์ ๋ณด๋ด์ง์ง ์์ (#quick-start)



## ๐RESTful API

### 	โญAPI

> Application Programming Interface 

- ์ฑ์ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด๊ฐ ์ ๊ณตํ๋ ๊ธฐ๋ฅ์ผ๋ก ์ํํ  ์ ์๊ฒ ๋ง๋  ์ธํฐํ์ด์ค

- ์๋ต ๋ฐ์ดํฐ ํ์ : HTML, XML, JSON

### 	โญREST

> REpresentational State Transfer

- API Server๋ฅผ ๊ฐ๋ฐํ๊ธฐ ์ํ ์ผ์ข์ ์ํํธ์จ์ด ์ค๊ณ ๋ฐฉ๋ฒ๋ก 
  - ๋คํธ์ํฌ ๊ตฌ์กฐ์๋ฆฌ์ ๋ชจ์
  - ์์์ ์ ์ํ๋ ๋ฐฉ๋ฒ์ ๋ํ ๊ณ ๋ฏผํ์

- REST์ ์์๊ณผ ์ฃผ์ ์ง์  ๋ฐฉ๋ฒ
  - ์์ : URI
  - ํ์ : HTTP Method
  - ํํ : ์์๊ณผ ํ์๋ฅผ ํตํด ๊ถ๊ทน์ ์ผ๋ก ํํ๋๋ ๊ฒฐ๊ณผ๋ฌผ, JSON์ผ๋ก ํํ๋ ๋ฐ์ดํฐ๋ฅผ ์ ๊ณต

- JSON (JavaScript Object Notation) : ๋ฌธ์์ด

  - ์ฌ๋์ด ์ฝ๊ฑฐ๋ ์ฐ๊ธฐ ์ฝ๊ฒ ๊ณ๊ธฐ๊ฐ ํ์ฑํ๊ณ  ๋ง๋ค์ด๋ด๊ธฐ ์ฌ์

  - ํ์ด์ฌ ๋์๋๋ฆฌ, ์๋ฐ์คํฌ๋ฆฝํธ ์ค๋ธ์ ํธ์ฒ๋ผ, C๊ณ์ด์ ์ธ์ด๊ฐ ๊ฐ๊ณ ์๋ ์๋ฃ๊ตฌ์กฐ๋ก

    ์ฝ๊ฒ ๋ณํํ  ์ ์๋ key-value ํํ์ ๊ตฌ์กฐ๋ฅผ ๊ฐ์ง

- **์ ๋ณด**๋ **URI**๋ก ํํ, **ํ์**๋ **HTTP Method**๋ก ํํ



## ๐Response

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

- **return ๊ฐ **: `JsonResponse` objects

  - JSON-encoded response ๋ง๋๋ HttpResponse ์ ์๋ฒ ํด๋์ค

    ```python
    return JsonResponse(articles_json, safe=False)
    ```

    ์ง๋ ฌํ : ๋ฐ์ดํฐ ๊ตฌ์กฐ๋ ๊ฐ์ฒด ์ํ๋ฅผ ๋์ผํ๊ฑฐ๋ ๋ค๋ฅธ ์ปดํจํฐ ํ๊ฒฝ์ ์ ์ฅํ๊ฑฐ๋ ๋์ค์ ์ฌ๊ตฌ์ฑํ  ์ ์๋ ํฌ๋งท์ผ๋ก ๋ณํํ๋ ๊ณผ์ 

- **return ๊ฐ ** : `HttpResponse`

  - ```python
    return HttpResponse(data, content_type='application/json')
    ```

- **return ๊ฐ** : `Django rest_framework`(DRF)

  1. **ModelSerialize** : Article ๋ชจ๋ธ์ ๋ง์ถฐ ์๋์ผ๋ก ํ๋๋ฅผ ์์ฑํด serialize ํด์ค

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

### 	โญDRF

|              | Django ModelForm | DRF (Django REST Framework) |
| ------------ | ---------------- | --------------------------- |
| **Response** | HTML             | JSON                        |
| **Model**    | ModelForm        | Serializer                  |

- Web API ๊ตฌ์ถ์ ์ํ Toolkit ์ ์ ๊ณตํ๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ

  > Web API : ์น ์ ํ๋ฆฌ์ผ์ด์ ๊ฐ๋ฐ์์ ๋ค๋ฅธ ์๋น์ค์ ์์ฒญ์ ๋ณด๋ด๊ณ  ์๋ต์ ๋ฐ๊ธฐ ์ํด ์ ์๋ ๋ช์ธ

- ModelForm๊ณผ ๋งค์ฐ ์ ์ฌํ ์ญํ 



## ๐ฅDRF๋ฅผ ์ด์ฉํ Single Model ์ค์ต

1. ๊ฐ์ํ๊ฒฝ ๋ฐ ํจํค์ง ์ค์น

2. ํ๋ก์ ํธ ์์ฑ

3. ์ฑ ์์ฑ ๋ฐ ๋ฑ๋ก

4. url ํ์ธ

5. ๋ชจ๋ธ ์์ฑ + makemigrations , migrate

   ```python
   from django.db import models
   class Article(models.Model):
       title = models.CharField(max_length=100)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   ![image-20220424165248675](0420%20REST%20API.assets/image-20220424165248675.png)

   - dummy data ์์ฑ

     ```bash
     $ python manage.py seed articles --number=5
     Unknown command: 'seed' #์๋ฌ
     ```

     ์๋ฌ :  seed ๊ฐ ์์

     ```bash
     $ pip install django_seed
     ```

     ๊ฐ์ ์๋ฌ : ์ฑ ๋ฑ๋ก ์๋์ด์์

     ```python
     # Application definition
     
     INSTALLED_APPS = [
         'articles',
         'django_seed',
     ```

     ์๋ฌ : `ModuleNotFoundError: No module named 'psycopg2'`

     ```bash
     $ pip install psycopg2
     ```

     ํด๊ฒฐ

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



5. serializers.py ์์ฑ

   ![image-20220424201827322](0420%20REST%20API.assets/image-20220424201827322.png)
   
   - ํด๊ฒฐ : field๊ฐ ์๋๋ผ fields



6. urls.py 

   1. ์ ์ฒด๊ฒ์๊ธ๋ชฉ๋ก
   2. ๊ฐ๋ณ๊ฒ์๊ธ์ `/<int:article_pk>/`ํ์

   

7. views.py 