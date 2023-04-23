import json


def top_company(movies):
    lst=[]
    for i in movies:
        id = i.get('id')
        id_json=open(f'data/movies/{id}.json',  encoding='utf-8')
        id_open=json.load(id_json)

        for j in id_open.get('production_companies'):
            lst.append(j.get('name'))

    counter = {}
    for k in lst:
        if k in counter:
            counter[k] +=1
        else: counter[k] =1
    counter = sorted(counter.items(), reverse=True, key=lambda item:item[1])

    return counter

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(f'배급한 영화가 많은 순으로 배급사 정렬하기\n{top_company(movies_list)}') 

