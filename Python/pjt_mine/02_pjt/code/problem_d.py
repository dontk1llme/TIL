import requests
from pprint import pprint

def recommendation(title):
    params = {'api_key':'38b9c36413ef2ab337be840d56d5bcda',
        'language':'ko',
        'region':'KR',
        'query':title
        }
        
    URL = 'https://api.themoviedb.org/3/search/movie'
    response = requests.get(URL, params=params).json()['results']
    title = []

    if len(response)==0: return None #검색한 영화 정보 없으면 none

    elif type(response[0]['id'])==int:
            id = response[0]['id']
            recURL=f'https://api.themoviedb.org/3/movie/{id}/recommendations'
            rec_response=requests.get(recURL, params=params).json()['results']

            for i in rec_response:
                title.append(i['title'])

            return title #추천 영화가 없으면 [], 있으면 그 목록 출력


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
