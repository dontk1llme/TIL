# [BAEKJOON] 2839 설탕배달
n = int(input())
bag=0
while n>=0:
    if n%5==0:
        bag = bag+n//5
        print(bag)
        break
    else:
        n = n-3
        if n<0:
            print(-1)
        bag+=1