#  [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합 (제출용) D3
# 비트연산!! https://velog.io/@jinho0705/SWEA-4837.-%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9%EC%9D%98-%ED%95%A9python
# https://scarletbreeze.github.io/articles/2019-07/SWE(4837)%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9_%ED%95%A9

# 비트연산
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1,13))
    ans = 0

    #부분집합 생성
    for i in range(1<<12):
        subset = []
        sum_v = 0
        for j in range(12):
            if i & (1<<j):
                subset.append(A[j])
                sum_v += A[j]
        if len(subset)==N and sum_v==K:
            ans+=1

    print(f'#{tc} {ans}')

# 재귀
# https://han-py.tistory.com/15

# 교수님 1
def dfs(n, cnt, sm):
    global ans
    #종료조건(정답만들기)
    if n==N:
        if cnt==CNT and sm==K:
            ans+=1
        return

    dfs(n+1, cnt+1, sm+lst[n]) #사용하는 경우
    dfs(n+1, cnt, sm) #사용하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    CNT, K = map(int, input().split())
    lst = list(range(1,13))
    N = len(lst)
    ans = 0
    #n, cnt, sum
    dfs(0,0,0)

    print(f'#{tc} {ans}')


#교수님 2 (가지치기 포함)
def dfs(n, cnt, sm):
    global ans
    #가지치기는 가장 위에서, 순서로는 가장 마지막
    if cnt>CNT or sm>K:
        return

    #종료조건(정답만들기)
    if n==N:
        if cnt==CNT and sm==K:
            ans+=1
        return

    dfs(n+1, cnt+1, sm+lst[n]) #사용하는 경우
    dfs(n+1, cnt, sm) #사용하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    CNT, K = map(int, input().split())
    lst = list(range(1,13))
    N = len(lst)
    ans = 0
    #n, cnt, sum
    dfs(0,0,0)

    print(f'#{tc} {ans}')