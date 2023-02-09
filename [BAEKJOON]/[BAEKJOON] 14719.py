# [BAEKJOON] 14719 빗물
# H*W 빈 배열 만들고 건물만큼 1로 채우기
# row별로 돌려서 1 찾고 그다음 1 찾고 그 사이를 2로 채우기 (1은 건물, 2는 비로 생각하기)
# 그다음 2 카운트하면 그게 답임.


W,H = map(int, input().split()) #H랑 W랑 반대로 생각햇더니 인덱스에러나서.. 걍 반대로함..귀찬아
block = list(map(int, input().split()))

rainarr = [[0]*H for _ in range(W)]  # H*W 빈 배열 만들고
for i in range(H):                     # 건물만큼 1로 채우기
    for j in range(block[i]):
        rainarr[j][i] = 1

cnt = 0 #출력할 답
for i in rainarr:
    bl=[] #block 인덱스 배열 만들기
    for j in range(H):
        if i[j] == 1:
            bl.append(j) #block은 1로 설정해뒀으니 있으면 인덱스 추가
    if len(bl)>1: #block이 한 row에 2개 이상이면
        r = [] #rain으로 채워야 되는 인덱스 배열
        for k in range(len(bl)-1): #block 사이에 채워야 돼서...
            r.extend(list(range(bl[k]+1,bl[k+1]))) #block 사이의 인덱스들 r 배열에 추가
        for l in r: #r만큼 rainarr을 수정하려 했으나(현재 주석한것들) 생각해보니 그냥 카운트 올려주면 됨.
            cnt+=1
    #         i[l]=2 #
    #
    # cnt+=i.count(2)

print(cnt)