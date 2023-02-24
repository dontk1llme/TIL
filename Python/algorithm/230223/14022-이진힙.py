#  [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 (제출용) D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = map(int, input().split())

    #최소힙에 데이터를 저장
    h =  [0]*(N+1)
    last = 0
    for n in lst:
        last+=1
        h[last]=n #가장 끝위치에 데이터 삽입
        #부모노드가 있고, 나보다 크면 교환
        c = last
        while 0<c//2 and h[c//2]>h[c]:
            h[c//2], h[c] = h[c], h[c//2]
            c//=2

    # last의 조상노드들의 합을 저장
    ans = 0
    c = last//2
    while c>0: #존재하는 조상인 경우
        ans+=h[c]
        c//=2 #기준점을 부모노드로 이동


    print(f'#{tc} {ans}')
