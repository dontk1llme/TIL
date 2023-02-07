#swea 1954

T = int(input())

#달팽이 우->하->좌->상
dr = [0,1,0,-1] #하, 상
dc = [1,0,-1,0] #우, 좌

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)] #달팽이 틀

    r,c=0,0 #초기위치
    d = 0 #0: 우, 1: 하, 2:좌, 3:상(인덱스)

    for n in range(1, N*N+1):#숫자 범위
        arr[r][c]=n
        r += dr[d]
        c += dc[d]

        #범위 벗어남 or 값 이미 있으면 방향 바꾸기
        if r<0 or c<0 or r>=N or c>=N or arr[r][c]!=0:
            #하나 빼서 원위치 하고 다음 거 실행할 거니까
            r -= dr[d]
            c -= dc[d]
            d = (d+1)%4 # 1 더해주고 안나누면 계속 커져서 나머지로
            r += dr[d]
            c += dc[d]

    print(f'#{tc}')
    for row in arr:
        for col in row:
            print(col, end=' ') #출력 *row로 하면 틀리고 왜 이렇게 하니까 맞냐
        print()




# https://jennnn.tistory.com/3
