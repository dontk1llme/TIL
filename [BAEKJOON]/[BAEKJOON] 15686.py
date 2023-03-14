# boj 15686 치킨 배달
# M개의 2만 남기고 거리 최소화.
# 하나씩 없애보고 가장 가까운 치킨집 찾아서 거리 재서 합으로 최소값 갱신 (DFS)
#콤비네이션 쓰는 방법도 있는 거 같은데 내가 안 써 봐서 참고만 했음
# https://alreadyusedadress.tistory.com/323 combi
# https://hardenkim.github.io/boj/boj-15686/ dfs
# 현재 치킨집 포함하는 경우와 안 포함하는 경우 나눠서 해줘ㅇㅑ함



N, M = map(int, input().split()) #도시, 최대 치킨집 개수
# lst = [list(map(int, input().split()) for _ in range(N))] #1 집 2 치킨 #전체리스트 필요없
ans = int(1e9) #최소값 비교해야 하니까
house = [] #집 좌표
chi = [] #치킨집 좌표
v = [] #visited


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chi.append((i, j))

def dfs(idx, cnt):
    global ans
    if idx>len(chi): #치킨집 다 돌았으면 종료
        return
    if cnt == M: # totaldis에 쌓아 주다가 최대 치킨집 수랑 같으면...
        total_dis = 0
        for r1, c1 in house:
            dis = int(1e9)
            for i in v: #집과 가장 가까운 치킨집과의 거리
                r2,c2 = chi[i]
                dis = min(dis, abs(r1-r2)+abs(c1-c2))
            total_dis += dis
        ans = min(ans, total_dis)

    # v: 유효한 치킨집의 인덱스
    v.append(idx) #현재 치킨집 포함
    dfs(idx+1, cnt+1)
    v.pop() #현재 치킨집 포함 x <- 경우 나눠서 해줘야함
    dfs(idx+1, cnt)


dfs(0,0)
print(ans)
