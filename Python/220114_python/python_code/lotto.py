#random 모듈 불러오기
import random

#숫자 통 (1,45)
nums = range(1,46)

#숫자 통에서 6개를 sample
lotto = random.sample(nums,6)

#결과 출력
print(lotto)
print(type(lotto))