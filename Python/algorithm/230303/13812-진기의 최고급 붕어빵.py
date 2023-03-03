# 1860. 진기의 최고급 붕어빵 D3
# https://jennnn.tistory.com/4

T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int, input().split()) #자격몇명, M초, K개
    sec = list(map(int,input().split())) #언제 도착하는지 초, N개
    ans = 'Possible'
    cnt=0 #도착한 사람 수
    for t in sorted(sec): #sorted 해야함
        cnt+=1
        if cnt > (t//M)*K: #도착한 사람 수 > 만들어진 붕어빵 수
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')

