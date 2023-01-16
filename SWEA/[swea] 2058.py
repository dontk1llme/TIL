#SWEA 2058 #자릿수 더하기

n = int(input())
sum = 0
for i in range(0,4):
    if n<=0:
        break;
    j = n%10        #나머지
    n = int(n/10)   #값 바꾸기
    sum += j
print(sum)
