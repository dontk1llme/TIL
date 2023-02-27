#정원에 나무 심기
T = int(input())
for tc in range(1, T+1):
    # 입력
    N,M = map(int,input().split()) #행, 열, 100이하
    lst = [list(map(int, input().split())) for _ in range(N)] #정원
    sum = 0 #총 비용
    cnt = 0 #심은 나무의 수
    max = 0 #가장 비싼 나무의 가격
    col = 0 #가장 비싼 나무가 심어진 열

    for i in range(0,M,2):
        for j in range(N):
            sum+=lst[j][i]
            cnt+=1
            if lst[j][i] >= max: #가장 비싼 나무의 가격, 열 갱신
                max = lst[j][i]
                col = i+1 #인덱스니까 +1 해 줘야 열 출력

    print(f'#{tc} {sum} {cnt} {max} {col}')


