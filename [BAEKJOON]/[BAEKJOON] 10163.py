# [BAEKJOON] 10163 색종이
# 주어진 수 네 개 중 뒤에 두 개가 좌표 두 개가 아니라 너비,높이였네 

N = int(input())
paper = [[0]*101 for _ in range(101)]
for i in range(1,N+1):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1, x1+x2):
        for y in range(y1, y1+y2):
            paper[x][y]=i

for i in range(1,N+1):
    cnt = 0
    for x in range(101):
        for y in range(101):
           if paper[x][y]==i:
               cnt+=1
    print(cnt)
