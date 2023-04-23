# 별자리 사진 찍기

T = int(input())
for tc in range(1, T+1):
    #입력
    N,K,A,B = map(int, input().split()) #하늘크기, 영역크기, 초점
    sky = [list(map(str, input().split())) for _ in range(N)]
    cnt = -1 #확대 횟수
    stars = 0

    #별 개수 찾기
    for i in range(N):
        for j in range(N):
            if sky[i][j]=='*': stars+=1

    #영역별로 탐색
    while T:
        nk = K // 2
        nowstars=0
        try:
            for i in range(A-nk, A+nk+1):
                for j in range(B-nk, B+nk+1):
                    if sky[i][j] == '*': nowstars += 1
        except: #인덱스에러 -> 범위 밖인 경우 등등...
            break
        if stars!=nowstars: #별 개수가 다르면 break (다 안 찍힌 것)
            break
        cnt+=1
        K-=2

    print(f'#{tc} {cnt}')
