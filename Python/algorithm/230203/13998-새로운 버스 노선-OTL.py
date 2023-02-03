from collections import Counter
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #1 일반 2 급행 3 광역 / A 출발 / B 종점
    # A와 B 사이: A와 B 포함 아님!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #아ㅁㅊ 근데 "모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B정류장에는 반드시 정차한다."ㅍ  ㅋ ㅋ ㅋ
    bus = [list(map(int, input().split())) for _ in range(N)]
    newlst = []
    for i in bus:
        if i[0]==1:
            lstA = list(range(i[1], i[2]+1))
            newlst.extend(lstA)

        elif i[0]==2:
            lstB = []
            if i[1] % 2 == 0: #짝수
                for j in range(i[1], i[2]+1):
                    if j % 2 == 0: newlst.append(j)
                    #if j%2==0: lstB.append(j)
            else: #홀수
                for j in range(i[1], i[2]+1):
                    if j % 2 != 0: newlst.append(j)
                    #if j%2!=0: lstB.append(j)
        else:
            lstC = []
            if i[1] % 2 == 0: #짝수
                for j in range(i[1], i[2]+1):
                    if j % 4 == 0: newlst.append(j)  # 4의 배수만
                    #if j%4==0: lstC.append(j) #4의 배수만
            else: #홀수
                for j in range(i[1], i[2]+1): #3의 배수이면서 10의 배수가 아닌
                    if j % 3 == 0 and j % 10 != 0: newlst.append(j)
                    # if j%3==0 and j%10!=0: lstC.append(j)
    print(newlst)
    cntlst = Counter(newlst) #중복 개수 세서
    print(cntlst)
    maxlst = cntlst.most_common(n=1) #젤 많은거 뽑아서
    print(f'#{tc} {maxlst[0][1]}') #개수만 뽑기...

    # N이 3인 경우만 생각했다................ 그냥 전체 리스트 만들자...................
    # print(lstA , lstB , lstC)
    # newlst = lstA + lstB + lstC #다 더해서
    # cntlst = Counter(newlst) #중복 개수 세서
    # print(cntlst)
    # maxlst = cntlst.most_common(n=1) #젤 많은거 뽑아서
    # print(f'#{tc} {maxlst[0][1]}') #개수만 뽑기...
    #ㅅㅂ왜안되는거야

