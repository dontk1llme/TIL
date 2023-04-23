import json
from pprint import pprint


def movie_info(movies, genres):
    mvlst=[]
    for i in movies:
        gridls=i.get('genre_ids')
        newls=[]
        for k in gridls:
            for j in genres:
                if k == j['id']:
                    newls.append(j['name'])
        
        new_data = {
            'genre_names': newls,
            'id': i.get('id'),
            'title': i.get('title'),
            'poster_path':i.get('poster_path'),
            'overview':i.get('overview'),
            'vote_average': i.get('vote_average')
        }
        
        mvlst.append(new_data)
    return mvlst
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
