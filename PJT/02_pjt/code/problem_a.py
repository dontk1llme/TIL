import requests


def popular_count():

    params = {'api_key':'38b9c36413ef2ab337be840d56d5bcda',
        'language':'ko',
        'region':'KR'
        }
    URL = 'https://api.themoviedb.org/3/movie/popular'
    response = requests.get(URL, params=params).json()['results']

    count=0
    for i in response:
        count+=1

    return count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
