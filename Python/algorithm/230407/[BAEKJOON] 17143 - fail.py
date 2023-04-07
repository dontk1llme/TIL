# boj 17143 낚시왕
# 시뮬레이션 연습문제
# 개못하네 진짜............ 이거안돌아감 맞게 나오는 것도 잇지만 시간초과

# 격자판 안 만들고 그냥 숫자로 조진다
# dlst = [(0,0), (-1,0), (1,0), (0,1), (-1,0)]#1 위 2 아래 3 오 4 왼

R, C, M = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(M)] #r,c,s,d,z

ans = 0


man = 0 #사람위치
while man<=C:
    man+=1 #사람이동
    # 낚시하기
    fishkill=[]
    for i in lst:
        if i[1]==man:
            fishkill.append([i, lst.index(i)])

    if fishkill: # 정렬해서 젤 가까이 있는 놈 낚기
        fishkill.sort(key=lambda x: x[0])
        ans += fishkill[0][0][4]
        lst.pop(fishkill[0][1])

    # 상어 이동
    for l in lst:
        tmp = 0
        while tmp<=l[2]:
            if l[3]==1:
                l[0]-=1
                if l[0]==1:
                    l[3]=2
            elif l[3]==2:
                l[0]+=1
                if l[0]==R:
                    l[3]=1
            elif l[3]==3:
                l[1]+=1
                if l[1]==C:
                    l[3]=4
            elif l[3]==4:
                l[1]-=1
                if l[1]==1:
                    l[3]=3
            tmp+=1

    # 상어냠냠
    lst.sort(key=lambda x: x[0])
    i = 0
    while lst:
        if i+1==len(lst):
            break
        if lst[i][0]==lst[i+1][0] and lst[i][1]==lst[i+1][1]:
            if lst[i][4]>lst[i+1][4]:
                lst.pop(i+1)
            else:
                lst.pop(i)
            i = 0
        i+=1
print(ans)