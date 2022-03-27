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

>  행과 열 형태로 아이템을 배치하는 1차원 레이아웃 모델

- 이전까지 Normal Flow를 벗어나는 수단은  

  - Float 혹은 Position 에서 하기 어려웠던 (수동 값 부여 없이) 

  1. 수직 정렬 - line height 같은걸로 할 수 있었음
  2. 아이템의 너비와 높이 혹은 간격을 동일하게 `알아서` 배치하는 것을 할 수 있음

- 배치설정
  - flex - direction : row (main축이 행으로 된다 (가로))
    - flex-direction: column (main축이 열로 된다 (세로))
  - flex - wrap
  
- 공간 나누기
  - justify - content (main axis) < 많이 쓰임
  
    - flex-start : margin 오른쪽
      - 123을 묶는 relative(부모) 만들어놓고, 1,2,3각각 auto줘서
    - flex-end : margin 왼쪽
    - center: margin 양쪽에
      - 또다른 div로 작게 묶고 그 div의 margin을 auto로
    - space-between : item 사이에 남은 공간을 줌
    - space-around : 각각의 item의 좌우에 남은 공간을 균등하게 줌
    - space-evenly : 가질 수 있는 여백을 item에게 균등하게 줌
  
    
  
  - align - contect (cross axis)  (아이템이 한줄로 배치됐을 경우 알 수가 없다)
  
- 정렬
  - align - items (모든 아이템을 cross axis) < 많이 쓰임
  - align - self (개별 아이템)

<많이 쓰이는 거>

```html
.flex container(부모요소){
	display:flex
}
```

- flex에 적용하는 속성
  - flex - grow : 남은 영역을 아이템에 분배
  - order : 배치 순서



## 실습하면서 궁금한것

1. div가 머냐

   1. div안에 div는 머냐
      - div는 박스형태의 시멘틱, 박스안에 박스가 있는거지

2. border

   - border은 박스의 구성요소 중 테두리!

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