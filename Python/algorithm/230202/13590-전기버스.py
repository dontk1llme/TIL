T = int(input())
for tc in range(1, T+1):
    # K: 최대한 이동할 수 있는 정류장 수
    # N: 종점
    # M: 충전기가 설치된 정류장 수
    K, N, M = map(int,input().split())
    charge = list(map(int,input().split())) # 충전기가 설치된 정류장 번호
    ans = 0 #충전 횟수
    nowch=K #현재 전력(출발시 풀충전이니 K)
    c=0 #정류장 인덱스(더해줄거라서 선언함)
    for i in range(1, N+1):
        nowch -= 1
        # print(f'현위치: {i}, 현재전력:{nowch}, 충전횟수:{ans}')
        if nowch < 0:
            ans = 0
            # print('죽을래')
            break
        if i ==charge[c]:
            # print('충전장이다')
            # while c < len(charge)-1:#종점 전까지만...
            if c <= M - 2:
                if charge[c+1]-charge[c] > nowch or nowch==0: # 충전
                    # print('충전할게')
                    ans+=1
                    nowch=K
                c += 1  # 정류장 지나감
            else:
                if N - i > nowch or nowch==0:
                    # print('충전할게')
                    ans += 1
                    nowch = K

    print(f'#{tc} {ans}')

    # for range로 한칸씩 가기 반복
    #     갓으면 nowch 줄어듦
    #     if 충전기 도착
    #         if 현위치에서 다음 정륮장까지 남은 거리가 현재 남은 전력이랑 작으면 그냥감
    #         else nowch+K ans+=1
    #     if nowch<0: break return 0
