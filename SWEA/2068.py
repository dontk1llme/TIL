#SWEA 2068 #최대수 구하기

num = int(input())

for i in range(1, num+1):
    a = list(map(int,input().split()))
    print("#%d" %i, max(a))