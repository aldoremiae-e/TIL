import requests

# 1. URL
# 요청 변수 : ?name=michael
# URL = 'https://api.agify.io?name=michael'
for name in ['tom', 'john', 'jane']:
    URL = 'https://api.agify.io'
    params = {
        'name' : name
    }

# 2. 요청
response = requests.get(URL,params=params).json()
print(response)
