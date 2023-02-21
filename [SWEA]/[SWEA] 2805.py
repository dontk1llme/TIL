# 2805. 농작물 수확하기 D3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    start, end = N//2,N//2

    inc = True #증가할지 여부
    for i in range(N):
        for j in range(start, end+1):
            ans+=lst[i][j]

        if start == 0: inc = False #지금부터 줄어들게...
        if inc==True:
            start-=1
            end+=1
        else:
            start+=1
            end-=1

    print(f'#{tc} {ans}')
