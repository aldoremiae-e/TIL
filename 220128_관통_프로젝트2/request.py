import requests
from bs4 import BeautifulSoup

## 받아오기
    #r = requests.get(url)
## response content
    #r.text

# 1. 주소
# 정보가 있는 사이트 url 확인하다
URL = 'https://finance.naver.com/sise/'
# 2. 요청
#response = requests.get(URL)  
            ##  <Response [200]> <class 'requests.models.Response'> : 성공적으로 가져왔다! 404 내가잘못했다 /500 개발자가 잘못했다

response = requests.get(URL).text 
            ##  <class 'str'>
#print(response, type(response)) 

# 2-1. beautifulsoup (text -> 다른 객체)
#html 파일에 있는 데이터를 가져오기 위해서 활용
data = BeautifulSoup(response, 'html.parser')
print(type(data))
# 2-2. 내가 원하는 정보를 가지고 온다
kospi = data.select_one('#KOSPI_now')
print(kospi)