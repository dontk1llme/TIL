# boj 5636 이진 검색 트리
# 전위순회 -> 원본으로 -> 후위순회
#왼쪽노드<루트<오른쪽

import sys #이거 안하고 그냥 input() 하면 런타임 에러남 ㅁㅊ놈인가
sys.setrecursionlimit(10**9)

# 개수를 안줬는데 입력부터 난감하누 -> tryexcept
lst=[]
while True:
    try:
        lst.append(int(sys.stdin.readline()))
        # lst.append(int(input()))
    except: #엔터 두번치면 여기네
        break

def post(s,e):
    if s>e:
        return
    mid=e+1 #루트보다 큰 값이 존재하지 않을 경우를 대비
    #루트보다 큰 값이 존재하면 그 값을 기준으로 왼,오 트리 나눠주고 재귀
    for i in range(s+1, e+1):
        if lst[s]<lst[i]: #루트보다 커지면 오른쪽
            mid = i
            break
    post(s+1, mid-1)
    post(mid, e)
    print(lst[s])

post(0,len(lst)-1)