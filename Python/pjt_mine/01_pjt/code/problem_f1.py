import json


def top_90(movies):
    lst=[]
    for i in movies:
        id = i.get('id')
        id_json=open(f'data/movies/{id}.json',  encoding='utf-8')
        id_open=json.load(id_json)

        title=id_open.get('title')
        year=id_open.get('release_date')
        revenue = id_open.get('revenue')
        
        if year[2:3] == '9':
            lst.append([title,revenue])
    lst.sort(key=lambda x: -x[1])
    return lst



if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(f'90년대 개봉작 중 많은 수입을 올린 영화 순위\n{top_90(movies_list)}') 

