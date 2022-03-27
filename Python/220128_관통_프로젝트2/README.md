# 7기 관통 프로젝트 02

## 목록

| 파일      | 내용                                                         | 링크                                                      |
| --------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| project_a | 인기 영화의 개수를 출력                                      | [a]("C:\Users\bamxd\Desktop\pjt02\students\problem_a.py)  |
| project_b | popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력 | [b]("C:\Users\bamxd\Desktop\pjt02\students\problem_b.py") |
| project_c | 영화목록을 평점순으로 출력하는 함수를 완성                   | [c]("C:\Users\bamxd\Desktop\pjt02\students\problem_c.py") |
| project_d | 제공된 영화 제목을 기준으로 추천영화 목록을 출력             | [d]("C:\Users\bamxd\Desktop\pjt02\students\problem_d.py") |
| project_e | 영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력  | [e]("C:\Users\bamxd\Desktop\pjt02\students\problem_e.py") |



## project_a

1. 주소

   URL , path, params 를 이용해 requsts 로 response 저장

    \# params (이거는 get함수에 있는거고)= params(내가만든 딕셔너리) 

     response = requests.get(BASE_URL+path, params = params).json()

2. len으로 길이값 리턴



## project_b

1. 주소

2. 저장할 리스트를 초기화

   \# problem_a에서 가져온 영화목록의 갯수를 범위를 가지고 반복문을 돌림

3. 리스트 안의 딕셔너리 키 vote_average(type :float) 의 값과 8.0을 비교



## project_c

1. 주소

2. 저장할 리스트를 초기화

3. problem_a에서 가져온 영화목록의 갯수를 범위를 가지고 반복문을 돌림

   vote_average만 있는 리스트 생성

   ```python
   for idx in range(len(response['results'])): 
   
       		vote_args.append(response['results'][idx]['vote_average']) 
   
    
   ```

   ```python
   vote_args.sort(reverse=True) #내림차순 정렬
   vote_args = vote_args[:5] # 다섯개만 추출
   ```

4. top5 에다가 상위 5개만 for문으로 가져오기



## project_d

1. 드디어 .get('') 의 용도를 알았다.
2. 요청 / 예외처리 try-except 이용

```python
    try :
        movie_id = response['results'][0].get('id')
    except :
        return None

    URL = f'http://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    response2 = requests.get(URL, params = params).json()
```





## project_e

1. cast에 있는 배우만 가져오기
2. crew에 있는 감독만 가져오기
3. 새로운 딕셔너리 만들기

