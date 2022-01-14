#모듈 불러오기
import random

# 점심 메뉴 리스트를 만들고 (최소 3개 이상) 
lunch = ['KFC', '버거킹', '맥도날드']

today_menu = random.choice(lunch)

# 출력 해보자
print(today_menu)
print(type(today_menu))
# 실행은 python lunch.py