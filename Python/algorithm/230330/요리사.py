#  [모의 SW 역량테스트] 요리사 (제출용) D3
# 조합으로 해야 함! 순열로 하면 시간초과. 차이 잘 알고 있기.
# 쫌 헷갈리네 . . .
# https://epser.tistory.com/14

def synergy(c):
    score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            score+= lst[c[i]][c[j]]+lst[c[j]][c[i]]
    return score

def cook(idx, k):
    global ans
    if idx==N//2: #한 음식에 선택되는 재료 개수가 N//2임
        A,B = [],[]
        for j in range(N):
            if v[j]: #방문 내역이 있으면 A, 아니면 B에 저장
                A.append(j)
            else:
                B.append(j)
        rA = synergy(A)
        rB = synergy(B)
        if abs(rA-rB)<ans:
            ans = abs(rA-rB)
        return
    for i in range(k,N):
        if not v[i]:
            v[i]=1
            cook(idx+1, i+1)
            v[i]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N #중복 안 보기 위해
    ans = 40000
    cook(0,0)
    print(f'#{tc} {ans}')

#////////////////////////////////////////////////////
# https://swbeginner.tistory.com/entry/4012-%EB%AA%A8%EC%9D%98-SW-%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9A%94%EB%A6%AC%EC%82%AC