# 0509 vue CLI

[TOC]



## vue CLI 설치

```bash
$ npm install -g @vue/cli
```

- -g : global

```bash
$ npm run serve
```

- .vue 로 만들어진 코드를 => HTML/CSS/JS ( 웹 개발 기본 언어)



### SFC (Single File Component)

- 컴포넌트를 구성하는 것은 결국 HTML/CSS/JS

  - vue는 컴포넌트 단위로 코드를 관리함

  

## Babel

> 자바스크립트 컴파일러

- 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역해주는 도구



## Webpack

> static module bundler

- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모듈을 매핑하고, 내부적으로 종속성 그래프를 빌드



## Vue 프로젝트 구조

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



## Pass Props & Emit Events

### 컴포넌트 작성

- 컴포넌트 구조
  - 템플릿(HTML)
  - 스크립트(JS)
  - 스타일(CSS)

- 컴포넌트 등록

  1. 불러오기 import
  2. 등록하기 register
  3. 보여주기 print

  

### Props : 부모 - 자식간의 정보전달

<img src="0509%20vue%20CLI.assets/image-20220509175028983.png" alt="image-20220509175028983" style="zoom:50%;" />

- Static Props
- Dynamic Props
- Prop 이름 컨벤션
  - 선언 시 camelCase 
  - HTML 템플릿에서 kebab-case



### 단방향 데이터 흐름

- 모든 props는 하위 송성과 상위 속성 사이의 단방향 바인딩 형성
- 부모 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향은 되지 않음
- 부모 컴포넌트가 업데이트될 때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트 됨



### Emit event

> 자식이 부모에게 "다했어요!"라고 말하는 것



## Vue Router

