# 0406 Modelform



## 1. forms.py

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

1. fields = '__ all __'
2. fields = ['title', 'content']
3. include
4. exclude



## 2. CRUD - new / create

- urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    ]
```

app_name 사용 이유



- views.py

```python
def new(request):
    form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/new.html', context)

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail',article.pk)
```



- new.html

```django
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
```

csrf_token : 403에러

form.as_p : p 태그

