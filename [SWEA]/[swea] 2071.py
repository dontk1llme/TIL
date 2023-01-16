#SWEA 2071 #평균값 구하기 D1

num = int(input())

for i in range(1, num+1):
    a = list(map(int,input().split()))
    print("#%d" %i, round(sum(a)/10))