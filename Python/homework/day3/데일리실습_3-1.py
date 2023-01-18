# 1680. 데일리실습 3-1.for문을 활용하여 리스트 변환 예제
'''
예를 들어, apple,rottenBanana,apple,RoTTenorange,Orange이라는 문자열이 주어진 경우,
대체된 리스트는 ['apple', 'banana', 'apple', 'orange', 'orange'] 이어야 한다.
'''

str = list(map(str,input().split(',')))
newlist=[0]*len(str)

for i in range(0,len(str)):
    newlist[i]=str[i].lower()
    if 'rotten' in newlist[i]:
        newlist[i] = newlist[i].replace('rotten','')

print(newlist)
