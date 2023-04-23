#1682. 데일리실습 3-3. 딕셔너리로 구성된 리스트의 활용

infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

sum = 0
for i in range(len(infos)):
    sum+=infos[i]['age']

print(sum)
