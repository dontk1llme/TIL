# BOJ 2477 참외밭
#변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
#첨엔 다 그려주려고 어렵게 생각했는데 그냥 큰 네모에서 작은 네모 빼면 됨
#큰 네모는 max 해도 되는데 작은 네모 구할 때는 min 하면 안 됨. (작은 길이가 작은거 높이가 아닐수도 잇잔슴)
# south 두 개 사이에 잇는 east 길이가 가로, east 두 개 사이에 잇는 south 길이가 높이
# 시작점 따라 위 생각도 달라져야 함

K = int(input())
lst=[]
cnt=[0]*5 #몇 번 나왓는지 세어줄것
big, small = 1,1 #큰네모, 작은네모 넓이
for _ in range(6):
    d, l = map(int,input().split())
    lst.append((d,l))
    cnt[d]+=1


for i in range(len(lst)):
    if cnt[lst[i][0]]==1: #한번만 나옴 -> 큰 사각형의 너비/높이
        big*=lst[i][1]
        continue
    n = (i+1)%6
    nn = (i+2)%6
    if lst[i][0]==lst[nn][0]: # 나랑 다다음애랑 같으면 다음애가 작은사각형
        small*=lst[n][1]
print((big-small)*K)

# K = int(input())
# lst = [list(map(int, input().split())) for _ in range(6)]
# garo = []
# sero = []
# scnt, ecnt=0,0
# partgaro, partsero=0,0
# for i in range(len(lst)):
#     if lst[i][0]==1 or lst[i][0]==2:
#         garo.append(lst[i][1])
#         if lst[i][0]==1 and ecnt==0:
#             partgaro=lst[i+1][1]
#             ecnt+=1
#
#     elif lst[i][0]==3 or lst[i][0]==4:
#         sero.append(lst[i][1])
#         if lst[i][0] == 3 and scnt == 0:
#             partsero = lst[i+1][1]
#             scnt += 1
#
# all = max(garo)*max(sero)
# part = partgaro*partsero
# print((all-part)*K)
