#이동횟수 기준
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 두더지 머리 내미는 횟수
    r, c = map(int, input().split())  # 시작 망치 위치 (1초에 한 칸 이동 가능, 가로부터)
    point = 0  # 획득점수
    for i in range(N):
        a, b, k = map(int, input().split())  # a,b: 두더지 좌표, k: 내밀고 있는 시간

        if abs(r-a)+abs(c-b)<=k: #목적지까지 이동 가능한 경우
            r,c=a,b
            point+=1
        elif abs(c-b)<=k: #열만 가능, 행은 모자람
            rem = k-abs(c-b) #열방향 이동 후 남은 거리
            c=b
            if r>a:
                r-=rem
            else:
                r+=rem
        else: #열도 모자람
            if c>b:
                c-=k
            elif c<b:
                c+=k

    print(f'#{tc} {point}')
