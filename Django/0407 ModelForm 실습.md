# 0407 ModelForm 실습



## Admin 등록

- admin.py

```python
from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    
admin.site.register(Article, ArticleAdmin)   # 어드민사이트에등록해줘
```



- list_display admin 옵션을 사용합니다. 이 옵션은 객체의 변경 목록 페이지에서 열로 표시 할 필드 이름들의 튜플입니다.

## CRUD - Create만으로 Form만들기

- views.py

```python
def create(request):
    if request.method == 'POST':
        # DB 저장
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 폼이 비어있다면
            article = form.save()
            return redirect('articles:index')
    else:
        # 폼 생성 - new 역할
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)
```



- create.html

````django
{% extends 'base.html' %}

{% block body %}
  <h1> NEW </h1>
  <form action="{% url 'articles:create' %}" method="POST"> 
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" name="submit" id="submit" value="제출">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock body %}
````



## CRUD - Edit 없이 Update 

- views.py

```python
def update(request, pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == 'POST':
        # DB저장
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        #edit 역할 - 폼 생성
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html, context')
```

-  instance 역할





## Error

> DB 테이블에 pk가 존재하지 않을 때



### 505 : 서버개발자의 오류

![image-20220407104133987](0407%20ModelForm%20%EC%8B%A4%EC%8A%B5.assets/image-20220407104133987.png)



### 404 : 사용자의 오류 (로 만들어버리는 코드)

- views.py 

```python
from django.shortcuts import get_object_or_404,

def detail(request, pk):
    article = get_object_or_404(Article,pk=pk)
    #article = Article.objects.get(pk=pk)
    context ={
        'article':article,
    }
    return render(request, 'articles/detail.html', context)
```

​	 `get_object_or_404` : pk가 있을 때와 없을 때를 조건문으로 나눠주는 함수





![image-20220407104926630](0407%20ModelForm%20%EC%8B%A4%EC%8A%B5.assets/image-20220407104926630.png)





### 405 : POST요청이 들어와야 하는데, GET요청이 들어왔을 때

 