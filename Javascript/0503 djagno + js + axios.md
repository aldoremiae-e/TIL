# 0503 djagno + js + axios



좋아요를 누르면 장고에서 어떠한 흐름으로 처리가 되나요?

`요청 - likes - redirect -  목록페이지 요청 - 전체페이지로딩`



그렇다면 AJAX를 이용하면?

html form 이 아니라 axios를 통해서 비동기 요청을 보낸다.



## 에러 1

```django
<form class="likeForm" data-article-id="{{article.pk}}" action="{% url 'articles:likes' article.pk %}" method="POST">  
	...  
</form>

{% block script %}
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const forms = document.querySelectorAll('.likeForm')
  console.log(forms)

  forms.forEach( form => { 
    form.addEventListener('submit', function(event){
      event.preventDefault()
      console.log(event.target.dataset)
      const URL = `/articles/${event.target.dataset.articleId}/likes/`
      console.log(URL)
      axios.post(URL)
        .then(response => console.log(response))
        .catch(error => console.log(error))
    })
  })
    
</script>
{% endblock script %}
```



![image-20220503134900389](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220503134900389.png)