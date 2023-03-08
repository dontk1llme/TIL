import sys
sys.stdin = open('러시아국기같은깃발.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    max_ = 0

for white in range(0,N-2): # 이 for문을 외워두자!
    for blue in range(white+1,N-1):
        total = 0

        for i in range(white+1):
            for j in range(M):
                if arr[i][j] == 'W':
                    total += 1

        for i in range(white+1,blue+1):
            for j in range(M):
                if arr[i][j] == 'B':
                    total += 1

        for i in range(blue+1,N):
            for j in range(M):
                if arr[i][j] == 'R':
                    total += 1

        if max_ < total:
            max_ = total
print(f'#{tc} {N*M-max_}')