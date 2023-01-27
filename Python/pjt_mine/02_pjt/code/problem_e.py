import requests
from pprint import pprint


def credits(title):
    params = {'api_key':'38b9c36413ef2ab337be840d56d5bcda',
        'language':'ko',
        'region':'KR',
        'query':title
        }
        
    URL = 'https://api.themoviedb.org/3/search/movie' #SearchMovies
    response = requests.get(URL, params=params).json()['results']
    title = []
    
    if len(response)==0: return None #검색한 영화 정보 없으면 none
    elif type(response[0]['id'])==int: #getCredits
        id = response[0]['id']
        crdURL=f'https://api.themoviedb.org/3/movie/{id}/credits?'

        cast=requests.get(crdURL, params=params).json()['cast']
        direct=requests.get(crdURL, params=params).json()['crew']

        castname = []
        directname=[]

        for i in cast:
            if i['cast_id']<10: castname.append(i['original_name'])
        for j in direct:
            if j['department']=='Directing': directname.append(j['original_name'])
        
        answer={'cast':castname, 'directing':directname}
        return answer






# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
