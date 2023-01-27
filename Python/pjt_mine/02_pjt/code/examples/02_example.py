# requests 사용 예시 2

import requests


URL = 'https://api.agify.io'

# params = https://api.agify.io?name=micheal&country_id=KR 하면 아래랑 같음

params = {
    'name': 'michael',
    'country_id': 'KR',
}

response = requests.get(URL, params=params).json()
print(response)
