# BOJ 2304 창고 다각형
# L 기준 오름차 정렬
# 현 L보다 큰 다음 L이 나올 때까지 H를 더해주면 되지않을까요?
# max값 나오면 끝에서부터 반대로...
# 왤케 더러운거같지....

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)] #L,H
lst.sort(key = lambda x:x[0]) #L 기준 오름차 정렬

#아 귀찬내 그냥 그래프 만들어
graph = [0]*(lst[-1][0]+1)
for i in lst:
    graph[i[0]] = i[1]

max_idx = graph.index(max(graph)) #최대값 인덱스

for i in range(max_idx): #최대값 이전까지
    if graph[i]>=graph[i+1]:
        graph[i+1]=graph[i]

for i in range(len(graph)-1,max_idx+1,-1): #최대값 이후부터는 뒤에서
    if graph[i]>=graph[i-1]:
        graph[i-1]=graph[i]

ans = sum(graph)
print(ans)





