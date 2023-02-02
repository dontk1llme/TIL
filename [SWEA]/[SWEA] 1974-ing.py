#1974. 스도쿠 검증 D2

T = int(input())
for tc in range(1, T+1):
    ans = 0
    jb = [1,2,3,4,5,6,7,8,9]
    #2차원 배열 입력받기
    sdk = [list(map(int, input().split())) for _ in range(9)]

    # ㅇ얘네 이거 이렇게 하나씩 하면 안되는거같은데???? 세 경우 다 한번에 봐야되는거 같은데
    
    #가로
    for i in range(len(sdk)):
        ls1 = sorted(sdk[i])
        if list(jb)==ls1: ans=1
        

    #세로
    collst=[[0]*9 for _ in range(9)]
    for i in range(len(sdk)):
        for j in range(len(sdk)):
            collst[i][j]=sdk[j][i]
        print(collst[i])
        ls2 = sorted(sdk[i])
        if list(jb)==ls2: ans=1
    
            
    #칸




    print(f'#{tc} {ans}')