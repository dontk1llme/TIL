#  직사각형과 점 (제출용) D3
# 2차원배열 만들어서 내부 1 경계 2 외부 0으로 채우기 (외부면 인덱스에러 나려나? -> ifelse 처리
# 런타임에러... 어뜨캄? 배열 써서 그런가 ㅇㅇ맞음

T = int(input())
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input()) #점 개수
    dot = [list(map(int, input().split())) for _ in range(N)]

    indot = 0 # 1. 점이 완전히 직사각형 내부에 있다.
    ondot = 0 # 2. 점이 직사각형의 네 변 중 적어도 하나의 위에 있다.
    outdot = 0 # 3. 점이 완전히 직사각형 외부에 있다.

    #배열 안 쓰고 해 본 거
    for d in dot:
        i,j = d[0], d[1]
        if x1<=i<=x2 and y1<=j<=y2:
            if i==x1 or j==y1 or i==x2 or j==y2: ondot+=1
            else: indot+=1
        else:
            outdot+=1

    print(f'#{tc} {indot} {ondot} {outdot}')



    #배열 써서 해 본 거
    # #사각형 배열
    # arr = [[0]*(x2+1) for _ in range(y2+1)]
    # for i in range(x1, x2+1):
    #     for j in range(y1, y2+1):
    #         if i==x1 or j==y1 or i==x2 or j==y2:
    #             arr[i][j]=2
    #         else: arr[i][j]=1
    #
    # #dot 검사
    # for d in dot:
    #     i,j = d[0], d[1]
    #     if 0<=i<=x2 and 0<=j<=y2:
    #         if arr[i][j] == 2: ondot+=1
    #         elif arr[i][j]==1: indot+=1
    #     else:
    #         outdot+=1