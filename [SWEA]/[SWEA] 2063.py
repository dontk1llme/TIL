#SWEA 2068 #중간값 찾기 D1

n = int(input())
a = list(map(int, input().split()))
a.sort()
i = (n-1)//2
print(a[i])