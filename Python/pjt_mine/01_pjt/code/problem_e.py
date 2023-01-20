import json


def dec_movies(movies):
    lst=[]
    for i in movies:
        id = i.get('id')
        id_json=open(f'data/movies/{id}.json',  encoding='utf-8')
        id_open=json.load(id_json)

        title=id_open.get('title')
        month=id_open.get('release_date')
        
        if month[5:7] == '12':
            lst.append(title)

    return lst
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
