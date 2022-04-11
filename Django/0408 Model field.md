# 0408 Model field

## Django에서 HTTP요청을 처리하는 방법

1. Django shortcut functions

   1. render()
   2. redirect()
   3. get_object_or_404()
   4. get_list_or_404()

2. View decorators

   1. `require_http_methods()` - 여러개를 사용할 수 있음 

      ex ) 'GET, POST' 만 활용하는 경우 : 

   2. `require_POST()` - POST만 활용하는 경우 - delete

   3. `require_safe()` : GET만 활용하는 경우 - index, detail

      => 조건에 맞는 요저

## ImageField

![image-20220408114441533](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220408114441533.png)

- False가 디폴트

- upload_to argument 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법을 제공

  - 문자열 값이나 경로 지정
  - 함추 호출

  ![image-20220408114859259](0408%20Model%20field.assets/image-20220408114859259.png)



주의사항

![image-20220408115221363](0408%20Model%20field.assets/image-20220408115221363.png)





- 궁금했던거 __ str() __ 정의

  - 객체 출력할 때 어떻게 보여줄지를 정의하는 방법

  - 클래스 안의 속성값만을 사용할 것이면, 굳이 적을 필요 없음!

    ```python
    def __str__(self):
        return f'Article 미애 <(self.id)>'
    ```

  - 