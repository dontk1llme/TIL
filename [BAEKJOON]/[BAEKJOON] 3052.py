# [BAEKJOON] 3052 나머지

lst = [0]*10
for i in range(10):
    N = int(input())
    lst[i]=N%42
lst = set(lst)
print(len(lst))