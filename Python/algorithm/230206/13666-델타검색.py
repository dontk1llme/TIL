T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] #입력받고

    di = [0,0,-1,1]
    dj = [-1,1,0,0]

    sum = 0
    for i in range(N):
        for j in range(N): #전부 다 돌기
            for k in range(4): #상하좌우라서 네번
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<N and 0<=nj<N: #유효한 인덱스이면
                    sum += abs(arr[i][j] - arr[ni][nj])
    
    print(f'#{tc} {sum}')

# https://5-ssssseung.tistory.com/24
# https://pika-chu.tistory.com/233

