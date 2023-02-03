#swea 5789 현주의 상자 바꾸기 D3

T = int(input())
for tc in range(1, T+1):
    N,Q = map(int, input().split()) #N: 박스 개수, Q: 변경 횟수
    box = [0]*N 
    for i in range(1,Q+1): #i는 1부터 시작
        L,R = map(int, input().split()) # L: 시작 상자, #R: 끝번 상자
        for j in range(L-1,R): #인덱스는 하나가 적다...
            box[j]=i

    print(f'#{tc}', end=' ')
    print(*box)
