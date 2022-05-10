## 0510 Vue Router

[TOC]



### 설치

```vue
$ vue add router
```

- git을 사용하고 있을 때 이런 질문을 해준다

  ![image-20220510093606531](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220510093606531.png)



### index.js

- 라우트에 관련된 정보 및 설정이 작성되는 곳

  ```javascript
  import HomeView from '../views/HomeView.vue'
  // 1. 불러와서
  import LottoView from '../views/LottoView.vue'
  import LunchView from '../views/LunchView.vue'
  Vue.use(VueRouter)
  // 2. 추가한다
  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/lotto/:lottoNum',
      name: 'lotto',
      component: LottoView
    },
    {
      path: '/lunch',
      name: 'lunch',
      component: LunchView
    }
  ]
  ```

  

### router-link

- 사용자 네비게이션을 가능하게 하는 컴포넌트

- 목표 경로는 `to` prop으로 지정

  ```vue
  /*App.vue*/
  
  <template>
    <div id="app">
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link :to="{ name: 'lotto', params: {lottoNum: 6} }">Lotto</router-link> |
        <router-link :to="{ name: 'lunch'}">Lunch</router-link>
      </nav>
      <router-view/>
    </div>
  </template>
  ```

  - router-view
    - 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
    - 실제 component가 DOM에 부착되어 보이는 자리를 의미

  

**History API**

- HTML History API를 사용해서 router를 구현한 것

- 브라우저의 히스토리는 남기지만, 실제 페이지는 이동하지 않는 기능을 지원

- 페이지를 다시 로드하지 않고, URL을 탐색할 수 있다!!

  *DOM의 Window 객체는 history객체를 통해 브라우저의 세션 기록에 접근할 수 있는 방법 제공*

  *history객체는 사용자를 자신의 방문 기록 앞과 뒤로 보내거나, 기록의 특정 지점으로 이동하는 등 유용한 메서드와 속성을 가짐*



1. Named Routes

   - 이름을 가지는 라우트

   - 명명된 경로로 이동하려면 객체를 vue-router 컴포넌트 요소의 prop에 전달

     ![image-20220510122022732](0510%20Vue%20Router.assets/image-20220510122022732.png)



2. 프로그래밍 방신 네비게이션

   - 선언적 방식

     ```
     <router-link :to='{name: 'home'}'>Home</router-link>
     ```

     

   - 프로그래밍 방식

     ```js
     // literal string path
     router.push('home')
     // object
     router.push({path: 'home'})
     // named route
     router.push({name: 'user', params: {userId: '123'}})
     // query, resulting in /register?plan=private
     router.push({path: 'register', query: {plan: 'private'}})
     ```

     <br>

   - 이동 로직

     ```
     this.$router.push({name: 'home'})
     ```



3. Dynamic Route Matching

   - 동적 인자 전달 `:` 이용
   - 주어진 패턴을 가진 라우트를 동일한 컴포넌트에 매핑해야하는 경우
   - 컴포넌트에서 `this.$route.params`

   

<hr>



## Youtube Project



### Youtube Project 컴포넌트 관계

![image-20220510134841831](0510%20Vue%20Router.assets/image-20220510134841831.png)



데이터를 활용하기 위해 필요한 패키지 => axios

axios에서 API를 활용하려면 url 필요!