# 0303 Django-first 실습

## 처음 실행

### 1. 가상환경

> 프로젝트별로 pip로 설치되는 패키지를 독립적으로 관리하기 위하여 

#### 가상환경 생성

```bash
$ python -m venv venv
```

#### 가상환경 실행

* `venv` 폴더 내의 스크립트를 실행 시키는 것

```bash
$ source venv/Scripts/activate
(venv)
```

#### 가상환경 종료

```bash
$ deactivate
```

### 2. Django 설치

```bash
$ pip install django==3.2.12
```

* 혹시라도 4.x 버전을 설치한 경우 삭제 후 재설치 

```bash
$ pip uninstall django
```

### 3. project 생성

```bash
$ django-admin startproject 프로젝트이름
```

### 4. app 생성

```bash
$ python manage.py startapp 앱이름
```

* app  생성을 하면, 바로 등록을 진행한다.

```python
# firstpjt/settings.py
INSTALLED_APPS = [
    '앱이름',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

### 5. Django 서버 실행

* 서버 종료는 `ctrl + c` 로 한다.

```bash
$ python manage.py runserver
```

![image-20220302130917374](0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220302130917374.png)

### 6. Django 개발하기

> 각 App에 MTV에 해당하는 기능을 구현한다.



## 주석 조건문 반복문

#### 주석

![image-20220303102217301](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220303102217301.png)

#### 조건문

![image-20220303102237941](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220303102237941.png)

#### 반복문

![image-20220303102312247](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220303102312247.png)

#### 필터

![image-20220303102349577](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220303102349577.png)



## template 활용하기

### form

- urls

  ```python
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('dinner/', views.dinner),
      path('greeting/', views.greeting),
      path('index/', views.index),
      path('lotto/', views.lotto),
      path('lunch/', views.lunch),
      path('throw/', views.throw),
      path('catch/', views.catch),
  ]
  ```

  

- views

  ```python
  def throw(request):
      return render(request, 'throw.html')
  
  def catch(request):
      message = request.GET.get('message')
      context = {
          'message' : message
      }
      return render(request, 'catch.html',context)
  ```

  

- template 에 form 양식

  ```django
  {% comment %}
  form 
    - action  : 폼을 처리할 url
    - method  : get / post
  
    input 
    - id : label for 연결
    - type : 다양한 타입 (radio, text, email, password)
    - name : 값(value)을 담는 이름 (변수이름)
  
    label
  - for : input id 연결
  {% endcomment %}
  
  <form action= "/catch/" method="GET">
    <label for="message">메세지:</label>
    <input type="text" id="message" name="message">
    <input type="submit" value="얍!">
  </form>
  ```

   

- form은 이렇게 작동 된다!

<img src="0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220303104842994.png" alt="image-20220303104842994" style="zoom:200%;" />

/catch/ : 앞 / 는 상대경로 뒤 / 는 관용구

/ : 초기 경로

/catch : catch페이지

/lotto : lotto페이지

...

### id , name ,url 관리

#### <절대경로/blog /id>![image-20220303111033286](0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220303111033286.png)



#### <절대경로/hello/이름>

![](0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220303124029456.png)



#### <각각의 앱(template)의 urls 를 관리하자>

![image-20220303112812593](0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220303112812593.png)

![image-20220303125551399](0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220303125551399.png)



ㄴ

![image-20220303132902309](0303%20Django-first%20%EC%8B%A4%EC%8A%B5.assets/image-20220303132902309.png)