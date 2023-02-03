T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #1 일반 2 급행 3 광역 / A 출발 / B 종점
    bus = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0]*1001

    for i in bus:
        if i[0]==1:
            for j in range(i[1], i[2]+1):
                cnt[j]+=1

        elif i[0]==2:
            if i[1] % 2 == 0: #짝수
                for j in range(i[1], i[2]+1):
                    if j%2==0:
                        cnt[j]+=1
            else: #홀수
                for j in range(i[1], i[2]+1):
                    if j%2!=0:
                        cnt[j]+=1

        else:
            if i[1] % 2 == 0: #짝수
                for j in range(i[1], i[2]+1):
                    if j%4==0:
                        cnt[j]+=1

            else: #홀수
                for j in range(i[1], i[2]+1): #3의 배수이면서 10의 배수가 아닌
                    if j % 3 == 0 and j % 10 != 0:
                        cnt[j]+=1

    print(f'#{tc} {max(cnt)}')

    #아직도 난 왜안되는지 모르겟음
    #천번 돌리고싶지 않앗는데...
