#SWEA 1209 [S/W 문제해결 기본] 2일차 - Sum D3

row, col = 100, 100

out=[]

for t in range(10):
    time=int(input())
    #2차원 배열 입력받기
    arr=[]
    for i in range(row):
        arr.append(list(map(int, input().split())))
        
    maxw=0 #가로
    maxl=0 #세로
    for r in range(row):
        sumw=0;suml=0;sum1=0;sum2=0
        sum1+=arr[i][i]
        sum2+=arr[i][99-i]
        for c in range(col):
            sumw+=arr[r][c] #좌->우 대각선
            suml+=arr[c][r] #우->좌 대각선
        
        if sumw>maxw: maxw=sumw 
        if suml>maxl: maxl=suml
    print(f'#{time} {max(maxw, maxl, sum1, sum2)}')

