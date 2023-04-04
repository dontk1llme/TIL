# 2832 [모의 SW 역량테스트] 미생물 격리 (제출용) D4
# 시뮬레이션!
# 고려 1. 약품에 닿앗나 -> 0이나 N-1 좌표 확인 / 고려 2: 겹쳣나: x,y 같은지 확인
# 이차원배열에 넣어서 해주려고 햇는데 안그래도 될거같음 걍 좌표만 다루기
# https://velog.io/@mingjuu_u/SWEA-2382.-%EB%AF%B8%EC%83%9D%EB%AC%BC-%EA%B2%A9%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 왜 나오다가 마냐??????????????


T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split()) #N 셀 개수, M 격리시간, K 미생물 군집 개수
    lst = [list(map(int,input().split())) for _ in range(K)] #세로, 가로, 수, 방향

    for m in range(M):
        merge = [] #겹치는지 확인용
        for l in range(len(lst)): #이동시키기
            #1 2 3 4 상 하 좌 우
            if lst[l][3]==1:
                lst[l][0] -= 1
            elif lst[l][3]==2:
                lst[l][0] += 1
            elif lst[l][3]==3:
                lst[l][1] -= 1
            elif lst[l][3]==4:
                lst[l][1] += 1
            #약품 닿?
            if lst[l][0]==0 or lst[l][0]==N-1 or lst[l][1]==0 or lst[l][1]==N-1:
                lst[l][2] = lst[l][2]//2
                #이동방향 바꾸기! 얘는 idx[l][3]만 다뤄야지 멍처아
                if lst[l][3] == 1:
                    lst[l][3] = 2
                elif lst[l][3] == 2:
                    lst[l][3] = 1
                elif lst[l][3] == 3:
                    lst[l][3] = 4
                elif lst[l][3] == 4:
                    lst[l][3] = 3

        lst.sort(reverse=True)
        a = 1
        while True:
            if a>=len(lst):
                break
            else:
                if lst[a-1][0]==lst[a][0] and lst[a-1][1] == lst[a][1]:
                    lst[a-1][2] += lst[a][2]
                    lst.pop(a)
                else:
                    a+=1

    ans = 0
    for i in lst:
        ans += i[2]
    print(f'#{tc} {ans}')