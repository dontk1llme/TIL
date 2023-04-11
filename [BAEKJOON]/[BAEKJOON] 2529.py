# boj 2529 부등호
# 백트래킹 https://jinu0418.tistory.com/114

# 숫자 하나씩 append -> 부등호 만족하는지 확인
# 백트래킹 -> 중복 없어야 되니까 for문으로 (0~9)
# 최소, 최대: 처음 애가 최소, 마지막 애가 최대


n = int(input())
lst = list(map(str,input().split()))
maxx, minn = '', ''
visited = [0]*10

def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j

def solve(idx, s):
    global maxx, minn
    if idx==n+1: #정답 찾기
        if len(minn)==0:
            minn=s
        else:
            maxx=s
        return
    for i in range(10):
        if visited[i]==0:
            if idx==0 or check(s[-1], str(i), lst[idx-1]): #조건 조심
                visited[i]=True
                solve(idx+1, s+str(i))
                visited[i]=False

solve(0, "")
print(maxx)
print(minn)