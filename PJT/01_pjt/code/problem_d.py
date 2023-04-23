import json


def max_revenue(movies):
    lst=[]
    for i in movies:
        id = i.get('id')
        id_json=open(f'data/movies/{id}.json',  encoding='utf-8')
        id_open=json.load(id_json)

        title=id_open.get('title')
        revenue=id_open.get('revenue')
        lst.append([title, revenue])

    lst.sort(key=lambda x: -x[1])
    return lst[0][0]
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
