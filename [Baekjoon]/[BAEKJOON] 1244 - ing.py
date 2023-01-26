# [BAEKJOON] 1244. 스위치 켜고 끄기


#입력받기
swnum = int(input()) #스위치 개수
switch = list(map(int, input().split())) # 스위치 입력 (1: 켜짐, 0: 꺼짐)
switch.insert(0, '공백') #맨 마지막 출력은 인덱스 1~8까지 해야함. 얘 빼고
studentnum = int(input()) #학생 수
stlst = []                 # 학생 리스트 (성별, 정수)
for i in range(studentnum):
    stlst.append(list(map(int,input().split())))

def change(n): #스위치 바꾸는 함수.
    if n==0: return 1
    elif n==1: return 0

for k in stlst:
    if k[0]==1: #남학생(1): 받은 수의 배수인 인덱스의 스위치 상태 바꾸기
        for l in range(1,swnum+1):
            if l%k[1]==0: 
                switch[l]=change(switch[l])
        
        
    elif k[0]==2: #여학생(2): 받은 수를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 그 구간 스위치 상태 모두 바꿈 (항상 홀수)
        front, end = k[1]-1, k[1]+1
        switch[k[1]]=change(switch[k[1]])
        while(True):
            if front==0 or end>swnum: break # 예제 답은 나오는데 indexerror ->이 코드 추가해주니 해결
            elif switch[front]==switch[end]:
                switch[front]=change(switch[front])
                switch[end] = change(switch[end])
                front-=1
                end+=1
            else: break
for i in switch[1:]:
    if i==switch[len(switch)-1]: print(i)
    else: print(i, end=' ')








