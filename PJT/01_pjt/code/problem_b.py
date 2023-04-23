import json
from pprint import pprint


def movie_info(movie, genres):
    gridls=movie.get('genre_ids')
    newls=[]
    for i in gridls:
        for j in genres:
            if i == j['id']:
                newls.append(j['name'])

    new_data = {
        'genre_names': newls,
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path':movie.get('poster_path'),
        'overview':movie.get('overview'),
        'vote_average': movie.get('vote_average')
    }
    return new_data
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
