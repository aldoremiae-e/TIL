# 0308 Model

## 흐름 그림

> 오늘의 목표 게시판 만들기!!

<img src="0308%20Model.assets/image-20220308124322056.png" alt="image-20220308124322056" style="zoom:50%;" />



### 1. models. py

> Model - Class 만들기 혹은 변경시 - 속성: 필드(타입)
>
> ```python
> from turtle import update
> from django.db import models
> 
> # Create your models here.
> # models.Model을 상속 받아서 만든다.
> class Article(models.Model):
>     # Class 속성 : 데이터베이스의 필드(컬럼)
>     title = models.CharField(max_length=30)
>     content = models.TextField()
>     # 처음 추가할 때만 저장
>     created_at = models.DateTimeField(auto_now_add=True)
>     # 뭔가 변경될 때마다 저장
>     update_at = models.DateTimeField(auto_now=True)
> 
> # 변수의 이름을 짓는 패턴
> # CamelCase => Class
> # snake_case=> function, variable
> ```
>
> 

<img src="0308%20Model.assets/image-20220308125953181.png" alt="image-20220308125953181" style="zoom:50%;" />



### 2. $ python manage.py makemigrations

> Makemigragions : 마이그레이션(설계도) 파일 생성
>
> models.py 저장 후 migration 시작

```bash
$  python manage.py makemigrations
```



*참고 SQLite 설치* 

<img src="0308%20Model.assets/image-20220308130915837.png" alt="image-20220308130915837" style="zoom:50%;" />



### 3. $ python manage.py migrate

> migrate : 실제로 DB를 반영하는 작업

```bash
$  python manage.py migrate
```



### 4. 확인

> pk 값은 자동적으로id 값으로 부여가 되는 것 같다.

<img src="0308%20Model.assets/image-20220308130952518.png" alt="image-20220308130952518" style="zoom: 50%;" />



### # created_at, updated_at (시간) migration 하기

- models.py

  ```python
  # 처음 추가할 때만 저장
    created_at = models.DateTimeField(auto_now_add=True)
  # 뭔가 변경될 때마다 저장
    update_at = models.DateTimeField(auto_now=True)
    
  ```

  

- $ python manage.py makemigrations  (쓰고 1. enter, enter)

  > migration 파일 생성

  ```bash
   $ python manage.py makemigrations
   # 새로운 필드가 추가되었는데 기본 값이 없다.
   # 왜 문제된다? DB에 값이 필수로 설정되어 있어서. 빈 값은 존재할 수 없도록 되어 있어서.
  You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.
  # 옵션 
  # 1. 내가 지금 직접 디폴트값을 줄게 => 
  # 2. 미안. 나 종료하고 models.py에서 내가 직접 설정할게 
  1) Provide a one-off default now (will be set on all existing rows) 
  2) Quit, and let me add a default in models.pySelect an option: 1    
  # 디폴트 값을 파이썬 문법으로 유효한 것을 입력해.
  Please enter the default value now, as valid Python
  # 너 이거 DateTime인데.... 2022-03-08 13:17 직접 X 파이썬 코드로 할 수 있도록 도와줌
  # 엔터만 누르면 지금 너 timezone에 맞는 현재시간으로 해줄게
  You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
  The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now  
  Type 'exit' to exit this prompt[default: timezone.now] >>>
  Migrations for 'articles':  
  articles\migrations\0002_auto_20220308_1314.py    
  - Add field created_at to article    
  - Add field updated_at to article
  ```

  

- $ python manage.py migrate

  >  DB반영
  
  ```bash
  $ python manage.py migrate
  ```



- 결과

<img src="0308%20Model.assets/image-20220308132807992.png" alt="image-20220308132807992" style="zoom:50%;" />



## ORM -Query

> ORM : Object Relational Mapping : 객체-관계 매핑
>
> 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해어, 객체를 통해 간접적으로 데이터베이스의 데이터를 다룬다.
>
> 객체 - 객체 지향 프로그래밍은 **Class**를 사용
>
> 관계형 데이터베이스 - **테이블**을 사용



1. 장고 익스텐션 설치 및 앱 등록 , 실행

```bash
miae@DESKTOP-TSJ4J9N MINGW64 ~/Desktop/Django_0308
$ pip install ipython django-extensions
```

![image-20220308135033427](0308%20Model.assets/image-20220308135033427.png)

> _로 저장하는 것 주의

```bash
$ python manage.py shell_plus
```



### 쿼리 조회

#### all()

> 해당 클래스(테이블) 데이터 조회 => QuerySet (객체들로 구성된)

```python
In [1]: Ariticle.objects.all()
# => <QuerySet [<Article: Article object (1)>]>
```

- <img src="0308%20Model.assets/image-20220308141455301.png" alt="image-20220308141455301" style="zoom:50%;" />



#### get() 

>  단일데이터 조회 => 객체, 오직 primary key 로만 접근 가능!
>
>  에러 상황 : 1. 데이터 결과가 없을 때	2. 데이터 결과가 중복되었을 때

```python
In [23]: Article.objects.get(pk=1)
# Out[23]: <Article: Article object (1)>

In [24]: Article.objects.get(pk=100)
# Article matching query does not exist.

In [26]: Article.objects.get(title='제목')
# 객체가 하나만 있는 경우
	# Out[26]: <Article: Article object (1)>
# 객체가 여러개 있는 경우
	# MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```



#### filter()

> 여러데이터 조회 = > Out : Queryset (리스트같은애) 이라는 객체로 접근 가능

```python
Article.objects.filter(title='제목')
# Out[16]: <QuerySet [<Article: Article object (1)>]>
Article.objects.filter(title='제목')[0].content
# Out[17]: '내용'
Article.objects.filter(title='제목')[0].id
# Out[18]: 1
Article.objects.filter(title='제목')[0].created_at
# Out[19]: datetime.datetime(2022, 3, 8, 5, 14, 10, 367455, tzinfo=<UTC>)
```



### Update

```python
a2 = Article.objects.get(pk=2)
a2.title = '변경된 제목'
a2.save()
```



### Delete

```python
a3 = Article.objects.get(pk=3)
a3.delete()
```

<img src="0308%20Model.assets/image-20220308145251101.png" alt="image-20220308145251101" style="zoom: 50%;" />



## 게시판 만들기

### 1. Create

#### Index - 목록

- pages/views

  ```python
  from django.shortcuts import render
  from .models import Article
  
  # Create your views here.
  def index(request):
      # 모든 게시글을 출력
      articles = Article.objects.all()
      context = {
          'articles' : articles
      }
      return render(request, 'pages/index.html', context)
  
  ```

- index.html

  ```html
  {% extends 'base.html' %}
  {% block body %}
    <h1>안녕하세요</h1>
  
    {% for article in articles %}
      <p> {{ article.title }} </p>
      <hr>
    {% endfor %}
  {% endblock body %}
  
  ```

  

#### Create - New

>  form을 이용하여 new에서 내용을 던져 create에서 받기

- url

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('', views.index, name='index'),
      path('new', views.new, name='new'),
      path('create/', views.create, name="create" ),
  ]
  
  ```

  

- views

  ```python
  def new(request):
      return render(request, 'pages/new.html')
  
  def create(request):
      # 사용자의 입력을 받아서
      title = request.GET.get('title')
      content = request.GET.get('content')
      #  DB에 저장
      article = Article()
      article.title = title
      article.content = content
      article.save()
      # template에서 보여져야해
      context ={
          'article' : article
      }
      return render(request, 'pages/create.html', context)
  ```

  

- template

  - new.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1> NEW </h1>
    <form action="{% url 'pages:create' %}" method="GET">
      <label for="title">제목: </label>
      <input type='text' id='title' name='title'>
      <label for="content">내용: </label>
      <textarea id="content" name="content"></textarea>
  
      <input type='submit' value="제출">
    </form>
  {% endblock body %}
  ```

  - create.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>{{ article.id }}번째 글이 작성 완료되었습니다.</h1>
    <h2>{{ article.title }}</h2>
    <p>{{ article.content }}</p>
  {% endblock body %}
  ```

  

- 흐름 사진

- <img src="0308%20Model.assets/image-20220308162356062.png" alt="image-20220308162356062" style="zoom:50%;" />

  <img src="0308%20Model.assets/image-20220308162119229.png" alt="image-20220308162119229" style="zoom:50%;" />



- 출력 결과

<img src="0308%20Model.assets/image-20220308162257458.png" alt="image-20220308162257458" style="zoom:50%;" />

<img src="0308%20Model.assets/image-20220308162416544.png" alt="image-20220308162416544" style="zoom:50%;" />

<img src="0308%20Model.assets/image-20220308162431912.png" alt="image-20220308162431912" style="zoom:50%;" />

### 2. READ 

#### Index - 목록 링크

>  Variable roution (변수화) => 게시글마다 각자 다른 url을 써서 다른 링크로 들어갈 수 있도록!

- index.html

  ```html
  {% extends 'base.html' %}
  {% block body %}
    <h1>안녕하세요</h1>
  
    {% for article in articles %}
      <a href="{% url 'pages:detail' article.pk %}">
        <p> {{ article.title }} </p> 
      </a>
      <hr>
    {% endfor %}
  {% endblock body %}
  ```



#### Detail - variable routing

- urls.py

  > variable routing

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('<int:pk>/', views.detail, name='detail')
  ]
  ```

  

- views.py

  > article이라는 db에서 pk를 get 해서 가져와서 url에 쓸거임

  ```python
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      context ={
          'article' : article
      }
      return render(request, 'pages/detail.html', context)
  ```

  

- detail.html (template)

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>{{article.pk}}번 글</h1>
    <h2>{{article.title}}</h2>
    <p>{{article.created_at}}</p>
    <hr>
    <p>{{article.content}}</p>
  {% endblock body %}
  
  ```




### 3.Delete

- urls

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('<int:pk>/delete/', views.delete, name='delete')
  ]
  ```

- views

  ```python
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('pages:index')
  ```

  

### 4. Edit - Update

- urls.py

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('<int:pk>/edit/', views.edit, name='edit'),
      path('<int:pk>/update/', views.update, name='update'),
  ]
  ```

  

- views.py

  ```python
  def edit(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article' : article
      }
      return render(request, 'pages/edit.html', context)
  ```

  ```python
  def update(request, pk):
      title = request.GET.get('title')
      content = request.GET.get('content')
  
      article = Article.objects.get(pk=pk)
      article.title = title
      article.content = content
      article.save()
      return redirect('pages:detail', article.pk)
  ```

  - **에러**

    ![image-20220309010837967](0308%20Model.assets/image-20220309010837967.png)

    - 에러이유

      ```python
      article = Article().objects.get(pk=pk)
      ```

      Article() 은 인스턴스이고, Article은 클래스이다.

      인스턴스는 관리자에 액세스할 수 없고, 우리는 Article 클래스에 있는 객체를 pk에 맞는 정보를 article에 저장해야 한다.

    - **에러수정** 

    ```python
    article = Article.objects.get(pk=pk)
    ```

    

  

- edit.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1> Edit </h1>
    <form action="{% url 'pages:detail' article.pk %}" method="GET">
      <label for="title">제목: </label>
      <input type='text' id='title' name='title' value="{{article.title}}">
      <label for="content">내용: </label>
      <textarea id="content" name="content">{{article.content}}</textarea>
  
      <input type='submit' value="제출">
    </form>
  {% endblock body %}
  ```

  

### 5. Redirect

> 다시 다른 웹페이지로 돌아가도록 지시

![image-20220309012420931](0308%20Model.assets/image-20220309012420931.png)

```python
return redirect('articles:detail', article.pk) # **kwargs

#=> 동등한 표현 
return redirect('articles:detail', pk = article.pk) #*args
return redirect(f'/articles/{article.pk}/')
```

함수의 인자를 URL로 받아야하기 때문에 'pages:detail' 이런식으로 받는 형식을 따름.



<img src="0308%20Model.assets/image-20220308231225527.png" alt="image-20220308231225527" style="zoom:50%;" />

***상태코드 302*** : **하이퍼텍스트 전송 프로토콜 (HTTP)의 302 Found 리다이렉트 상태 응답 코드는 클라이언트가 요청한 리소스가 Location 헤더에 주어진 URL에 일시적으로 이동되었음을 가리킨다.**



## form 형식 속 method="GET->POST"

![image-20220308174615359](0308%20Model.assets/image-20220308174615359.png)

> 보통 POST를 쓴다.

get : 정보를 달라 => URL에 노출이 된다

post : 등록해라 ( id, password ) => URL에 숨겨서 볼 수 있도록

![image-20220308175010629](0308%20Model.assets/image-20220308175010629.png)