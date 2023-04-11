# boj 13023 ABCDE
# 그래프 + 백트래킹 https://data-flower.tistory.com/104

# dfs
def dfs(idx, depth):
    global ans
    visited[idx] =True
    if depth==4: #종료조건, 친구 관계 4번 이상 존재하면 답 있는 거
        ans = 1
        return
    for i in friends[idx]:
        if not visited[i]:
            visited[i]=True
            dfs(i,depth+1)
            visited[i]=False


N,M = map(int,input().split())
friends = [[] for _ in range(N)]    
visited = [0] * (N+1) #방문
ans = 0
for i in range(M): #그래프 만들기
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(N):
    dfs(i,0) #탐색
    visited[i]=False #방문표시 해제
    if ans:
        break

print(ans)