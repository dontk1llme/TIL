# BOJ 1931 회의실 배정

# 텀 짧은 것들 먼저
# 아 2차원배열로 하는 게 낫나??
# ㄴㄴ 안 나음 이거 그리디로 해야 한대

# https://suri78.tistory.com/26 정렬해야하는 이유 나와있음
# 1. 회의 종료 시간이 빨라야 함. (빨리 끝나야 많은 것들을 할 수 있음)
# 2. 회의 종료 시간이 같은 경우 시작 시간이 빨라야 함. (ex 1,2 2,2 하면 1부터 해야 2도 가능)


N = int(input())
meet = []
# start, end = 2**31-1,0 #시작시간, 종료시간 찾기
for tc in range(N):
    x,y=map(int, input().split())
    meet.append((x,y))
    # if start>=x: start=x      # 전혀 이렇게 하는거 아니네..
    # if end<=y: end=y
# time = [0]*(len(range(start,end))+1) #타임테이블

meet.sort(key=lambda x:x[0]) #시작 시간으로 먼저 정렬
meet.sort(key=lambda x:x[1]) # 종료 시간으로 정렬

cnt = 1
endtime = meet[0][1]
for i in range(1,N): #0은 이미 햇으니까 1부터
    if meet[i][0]>=endtime:
        cnt+=1
        endtime = meet[i][1]
print(cnt)
