# 혹시 같은 색깔이 겹쳐서 여러번 칠해진다면...
# color   1, 2, 3, 4, 5
tbl = [0, 1, 2, 4, 8, 16]
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 입력 사각형의 개수
 
    ans = 0
    arr = [[0]*10 for _ in range(10)]
    # [1] 해당 범위에 컬러값 누적
    for _ in range(N):  # N번 반복해서 칠하기
        R1,C1,R2,C2,color = map(int, input().split())
        for i in range(R1, R2+1):
            for j in range(C1, C2+1):
                arr[i][j] |= tbl[color]
 
    # [2] 보라색(==3)값의 개수 cnt
    for i in range(10):
        for j in range(10):
            if arr[i][j]==3:
                ans+=1
 
    print(f'#{test_case} {ans}')