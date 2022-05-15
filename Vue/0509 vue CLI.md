# 0509 Vue CLI

[TOC]

## Vue CLI 

> Vue.js 개발을 위한 표준 도구

- 프로젝트의 구성을 도와주는 역할을 하며, Vue 개발 생태계에서 표준 tool 기준을 목표로 함
- Bable(번역기), Webpack (bundler) 에 대한 초기 설정이 되어있음



### Node.js

> 자바스크립트는 브라우저를 조작하는 언어
>
> 브라우저 밖에서 자바스크립트를 사용할 수 있게 환경을 제공

- 자바스크립트를 브라우저가 아닌 환경(VScode)에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경

```bash
$ npm install -g @vue/cli
```



### npm : Node Package Manager

- 자바스크립트 언어를 위한 Node.js의 기본 패키지 관리자 
  - python- pip / Node.js - npm
  - pip 같이 다양한 의존성 패키지를 관리

- -g : global
  - python과 달리 개별로 설치되기 때문에, 전체 환경에 설치하기 위해서는 -g 필요
  - 앱에 따라 -g 로 할지 안할지 모르기때문에, 반드시 설치문서를 참고




- 프로젝트 생성 및 서버

```bash
$ vue create 앱이름	# 프로젝트 앱 생성
Default ([Vue 2] babel, eslint) # 버전 2로하기

$ cd 앱이름 	# 앱 이동
$ npm run serve		# 런 서버
```

- .vue 로 만들어진 코드를 => HTML/CSS/JS ( 웹 개발 기본 언어)



## SFC

> Single File Component

### Component

- 기본 HTML 엘리먼트를 **확장**하여 **재사용** 가능한 코드를 **캡슐화**하는데 도움을 준다

- 유지보수가 쉽고, 재사용 측면에서 강력한 기능을 제공

  

### SFC (Single File Component)

- Vue의 컴포넌트 기반 개발의 핵심 특징

  - 하나의 컴포넌트 :  하나의 `.vue` 파일 안에서 작성된 코드의 결과물
    - `.vue` 파일에서 HTML, CSS, JavaScript 코드를 한번에 관리

  - 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일(.vue)에서 관리
  - `.vue `확장자를 가진 `SFC` 를 통해 개발하는 방식
  - vue는 컴포넌트 단위로 코드를 관리한다!

  **Vue 컴포넌트 === Vue 인스턴스 === .vue파일(html,css,javascript)**



### Vue Component

- 단일 파일 관리 개발

  - 쉽게 개발할 수 있지만, 변수 관리와 유지보수가 힘듬

- 여러 컴포넌트(파일) 이 한 화면을 구성

  - 각 기능 별로 파일을 나눠서 개발 
    - 처음 개발을 준비하는 단계에서 시간 소요가 증가
    - 변수관리 용이, 기능 별 유지,보수비용이 감소


  <br>

- Vue Component 구조 : 사이클이 존재하지 않는 Tree 구조

  - 한 화면 안에서도 기능 별 컴포넌트가 존재

    - 하나의 컴포넌트가 여러개의 하위 컴포넌트를 가질 수 있다
    - Vue는 컴포넌트 기반의 개발 환경 제공!

  - Vue 컴포넌트 === Vue 인스턴스 (app)

    ```vue
    const app = new Vue({...})
    ```

    - **반드시 파일 단위로 구분되어야 하는 것이 아님!**
    - 단일 .html 파일 안에서도 여러 개의 컴포넌트를 만들어 개발 가능




## Babel

> 자바스크립트 컴파일러

- 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역해주는 도구

**`bable.config.js`**



## Webpack

> 모듈 간의 의존성 문제를 해결(Bundler)하기 위한 도구
>
> 다양한 Bundler 중 하나인 Webpack ;)

- Static **Module** Bundler

  - 모듈은 파일 하나를 의미한다 (JS파일 1개 === 모듈 1개)

  - 모듈 관련 문법 없이 JS사용

  - 라이브러리를 만들어 모듈이나 코드를 모듈단위로 작성

    ex ) ESM(ECMA Script Module), AMD(Asynchronous Module Definition), CommonJS, UMD



모듈의 수가 많아지고 모듈간의 의존성이 JS와 앱이 복잡해져서 **전역 scope를 공유하는 형태의 기존 개발 방식의 한계점 발생**



- **bundler**
  - 프로젝트에 필요한 모듈을 매핑하고, 내부적으로 종속성 그래프를 빌드
  - 여러 모듈을 하나로 묶어주고, 묶인 파일을 하나(혹은 여러개)로 합쳐짐
  - Bundling 된 결과물은 더 이상 순서에 영향받지 않고 동작하게 됨




## Vue 프로젝트 구조

<img src="0509%20vue%20CLI.assets/image-20220510013543185.png" alt="image-20220510013543185" style="zoom:67%;" />

1. node_modules 
   - (venv 같은 존재) 에 들어가 있음, ignore도 되어있음

2. public/index.html
   - Vue앱의 뼈대, 실제 제공되는 단일 html 파일
3. src/assets
   - webpack에 의해 빌드 된 정적 파일
4. src/components
   - 하위 컴포넌트들이 위치
5. src/App.vue
   - 최상위 컴포넌트

6. src/main.js
   - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
   - 실제 단일 파일에서 DOM과 data를 연결했던 것과 동일한 작업이 이루어짐
   - Vue 전역에서 활용할 모듈을 등록
7. babel.config.js
   - babel 관련 설정이 작성된 파일

8. package.json
   - (req.txt 같은 존재) 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션이 포함
9. package-lock.json
   - (req.txt 같은 존재) node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리, 의존성 패키지 충돌 방지



## Pass Props & Emit Events

### 컴포넌트 작성

- 컴포넌트 구조
  - 템플릿(HTML)
  
    - HTML 의 body 부분, 각 컴포넌트를 작성

  - 스크립트(JS)
  
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성
  
  - 스타일(CSS)
  
    
  
- 컴포넌트 등록

  1. 불러오기 import
  2. 등록하기 register
  3. 보여주기 print

  ```vue
  /* App.vue */
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <!-- 3.print -->
      <!-- 케밥 케이스 -->
      <the-about></the-about>
    </div>
  </template>
  <script>
  // 1. import
  import TheAbout from './components/TheAbout.vue'
  
  export default {
    name: 'App',
    // 2. register
    components: {
      TheAbout,
    }
  }
  </script>
  ```
  
  ```vue
  /* TheAbout.vue */
  <template>
    <h2>First Vue!</h2>
    
  </template>
  
  <script>
  export default {
    name : 'TheAbout'
  }
  </script>
  ```
  
  <img src="0509%20vue%20CLI.assets/image-20220510014801290.png" alt="image-20220510014801290" style="zoom:50%;" />
  
  

### Props & Event

> 부모 =**props**> 자식, 자식 =**event**> 부모 간의 정보전달

- 컴포넌트간 부모-자식 관계가 구성되며 이들 사이에 필연적으로 의사소통 필요

- 부모는 자식에게 데이터를 전달(Pass props)하고, 자식은 부모에게 메시지를 보냄(Emit event)

<img src="0509%20vue%20CLI.assets/image-20220509175028983.png" alt="image-20220509175028983" style="zoom:50%;" />

- Static Props

  1. 자식 컴포넌트에 보낼 prop 데이터 선언

     - 숫자 전달할 때 만드시 v-bind `:` 사용해야함

     ```vue
     /* App.vue */
     <the-about 
           my-message ='부모로부터 prop한 데이터'></the-about>
     ```

  2. 수신 할 prop 데이터 명시적 선언 후 사용

     - 내용이 여러개일 때 div로 묶어준다!

     ```vue
     /* TheAbout.vue */
     
     <template>
       <!-- template 안에는 반드시 하나의 Element(div)만 있어야 한다..  -->
       <div>
         <h1>{{ myMessage }}</h1>
     
     <script>
     export default {
       name: 'TheAbout',
       props: {
         // 키: 데이터 타입
         myMessage: String,
     </script>
     ```
     
     

- Dynamic Props

  1. **v-bind directive** 를 사용해 부모의 데이터의 props를 동적바인딩

  2. 부모의 데이터가 업데이트 될 때마다 자식 데이터로도 전달 됨

     ```vue
     /* App.vue */
     <template>
       <div id="app">
        <!--: 는 데이터를 걸어주는 애-->
        <the-about 
           :parent-data="parentData"
         ></the-about>
       </div>
     </template>
     
     <script>
     // 1. import
     import TheAbout from './components/TheAbout.vue'
     
     export default {
       name: 'App',
       // 2. register
       components: {
         TheAbout,
       },
       data: function() { 
         return {
           parentData: 'This is parent data to child component by v-bind'
         }
       },
     }
     </script>
     ```

     - parentData: 앞에 띄어쓰기하면 안됨

     - **컴포넌트의 data는 반드시 함수여야한다**

       - 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유하므로 새로운 data 객체를 반환하여야함
       
       

  3. 수신할 prop 데이터를 자식.vue에 명시적 선언 후 사용

     ```vue
     /* TheAbout.vue */
     
     <template>
       <div>
         <p>{{ parentData }}</p>
       </div>
     </template>
     
     <script>
     export default {
       name: 'TheAbout',
       props: {
         parentData: String,
       }
     }
     </script>
     ```
     
     

- Prop 이름 컨벤션
  - 선언 시 camelCase 
  - HTML 템플릿에서 kebab-case



### 단방향 데이터 흐름

- 모든 props는 하위 속성과 상위 속성 사이의 **단방향 바인딩** 형성
- 부모 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향은 되지 않음
- 부모 컴포넌트가 업데이트될 때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트 됨



### Emit event

> 자식이 부모에게 "다했어요!"라고 말하는 것

- `$emit(event-name)`

  *이름 컨벤션 : kebab-case 사용 권장*

  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스너의 콜백 함수로 전달

1. 현재 인스턴스(자식)에서 `$emit 인스턴스 메서드`를 사용해 이벤트를 트리거
   - v-model은 input으로 인해 바뀐 data를 걸어줌
   - 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유하므로 새로운 data 객체를 반환하여야 하기 때문에, data는 함수여야 한다.

```vue
/*TheAbout*/
<template>
  <!-- template 안에는 반드시 하나의 Element(div)만 있어야 한다..  -->
  <div>
    <input 
      type="text"
      v-model="childInputData"
      @keyup.enter="childInputChange"
    >
  </div>
```

```vue
<script>
export default {
  name: 'TheAbout',
  data: function () {
    return {
      childInputData: ''
    }
  },
  methods: {
    childInputChange: function(){
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>
```

2. 자식 컴포넌트에서 $emit('`event`', this.data)로 받은 이벤트를

   부모 컴포넌트에서 v-on:`event` 혹은 @`event`를 사용하여 청취

```vue
/*App.vue*/
<template>
  <div id="app">
    <the-about 
      @child-input-change="parentGetChange"
    ></the-about>
  </div>
</template>
```

```vue
<script>
// 1. 불러오기 (import)
import TheAbout from './components/TheAbout.vue'

export default {
  name: 'App',
  // 2. 등록하기 (register)
  components: {
    TheAbout,
  },
  methods: {
    parentGetChange: function (inputData) {
      console.log('Boss: 들리는군..', inputData)
    }
  }
}
</script>

```

<img src="0509%20vue%20CLI.assets/image-20220515232813063.png" alt="image-20220515232813063" style="zoom:50%;" />



## 정리

### SFC

- Vue 컴포넌트 === Vue 인스턴스 === new Vue({})

- Vue 인스턴스 === .vue 파일 안의 코드 집합
- HTML, CSS, JavaScript 를 .vue 확장자 파일 안에서 개발



### Vue CLI

- Vue CLI : Vue.js 개발을 위한 표준 도구
  - 프로젝트의 구성을 도와주는 역할을 하며, Vue 개발 생태계에서 표준 tool 기준을 목표로 함

- Node.js : 자바스크립트를 브라우저 밖에서 실행할 수 있는 환경 제공
- Babel : 자바스크립트 코드를 구버전으로 번역해주는 컴파일러
- Webpack : 모듈 간의 의존성 문제를 해결하기 위한 Bundler 중 하나
