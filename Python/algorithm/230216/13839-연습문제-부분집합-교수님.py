# Stack2_연습문제_2: 부분집합 (제출용) D3

#가능한 모든 경우 실행: 정답 -> Tree로 표현. 이진 or 멀티. 둘 다 가능하면 닥 이진
# Tree의 headnode: 무조건 종료조건에 관계된 것으로 설정. 여기에서는 배열의 index (정해진 끝이 존재함)
# dfs(n, sum, ) #n = 무조건 맨앞, 종료조건임. 그리고 들어가자마자 체크해야 함
# 종료조건을 쓰고 밑에 재귀호출 해야 함. 근데 호출할 때 무조건 n+1 해야함 그래야 언젠가 끝나니까
# 재귀는 슈더코드로 짜지마... 최대한 깔끔하게 짜...

#가지치기 안하기
def dfs(n, sm):
    global ans #재귀에서 웬만하면 글로벌 금지. 답만 디버깅용으로
    #종료조건 먼저 체크
    if n==N:
        if sm == K:
            ans +=1
        return
    #하부함수 호출
    dfs(n+1, sm+lst[n])#포함하는 경우
    dfs(n+1, sm) #포함하지 않는 경우

    return

T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0,0)

    print(f'#{tc} {ans}')


#가지치기 하기 -> 최소값 묻는 문제가 많음
# def dfs(n, sm):
#     global ans  # 재귀에서 웬만하면 글로벌 금지. 답만 디버깅용으로
#     if sm>K: #가지치기
#         return
#     # 종료조건 먼저 체크
#     if n == N:
#         if sm == K:
#             ans += 1
#         return
#     # 하부함수 호출
#     dfs(n + 1, sm + lst[n])  # 포함하는 경우
#     dfs(n + 1, sm)  # 포함하지 않는 경우
#
#     return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     lst = list(map(int, input().split()))
#     ans = 0
#
#     print(f'#{tc} {ans}')