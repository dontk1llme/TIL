#  [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합 (제출용) D3

def dfs(n, sm, c): #c: count
    global cnt #재귀에서 웬만하면 글로벌 금지. 답만 디버깅용으로
    #종료조건 먼저 체크
    if n==len(A): #전체 길이가 종료조건
        if sm == K and c==N: #sum이 K이고 count가 N과 같으면
            cnt +=1
        return
    #하부함수 호출
    dfs(n+1, sm+A[n], c+1)#포함하는 경우
    dfs(n+1, sm, c) #포함하지 않는 경우

    return

T = int(input())
A = list(range(1,13))

for tc in range(1, T+1):
    N,K = map(int, input().split())
    cnt = 0
    dfs(0,0,0)

    print(f'#{tc} {cnt}')
