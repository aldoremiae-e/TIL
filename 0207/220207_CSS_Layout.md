# 220207 CSS Layout

## float  

> 흐름(normal flow)로부터 떨어져 주변을 wrapping하도록 함

- Positioning : Normal flow를 벗어나도록 함
  - absolute (static이 아닌 부모)
  - fixed(브라우저 :viewpoint 기준)
- Float 속성
  - none : 기본값
  - left : 요소를 왼쪽으로 띄움
  - right : 요소를 오른쪽으로 띄움

```html
.left{
	float: left;
}
```

- 이후 요소에 대하여 Float속성이 적용되지 않도록 Clearing이 필수
  - ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
    - 보통 content속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 쓰임

```html
.clearfix::after{
	content: "";
	display: block;
	clear: both;
}
```



## Flexbox

>  이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position 에서 하기 어려웠던 (수동 값 부여 없이) 
>
> 1. 수직 정렬 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치하는 것을 할 수 있음

- 배치설정
  - flex - direction
  - flex - wrap
- 공간 나누기
  - justify - content (main axis) < 많이 쓰임
  - align - contect (cross axis)  < 머리를 돌려서 봐야함
- 정렬
  - align - items (모든 아이템을 cross axis) < 많이 쓰임
  - align - self (개별 아이템)

<많이 쓰이는 거>

```html
.flex container{

}
```

- flex에 적용하는 속성
  - flex - grow : 남은 영역을 아이템에 분배
  - order : 배치 순서



## 실습하면서 궁금한것

1. div가 머냐

   1. div안에 div는 머냐

2. border

   <style>
       border 은 머냐
   </style>

3. .left는 뭐고 clear - left 는 또뭐냐

   <style>
       /*기본적으로 right가 되어있나? 아래를 쓰면 요소를 왼쪽으로 띄워짐*/
   	.left{
   		float: left;
   	}
       .clear-left {
     		clear: left;
   	}
   </style>

4. float는 스타일로 직접쓰고 flex는 링크를 통해 css로 연결하는건가