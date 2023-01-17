#2072. 홀수만 더하기 D1

a = int(input())
for t in range(1,a+1):
    li = map(int, input().split())
    answer = 0
    for i in li:
        if i%2 !=0:
            answer += i
    print("#"+str(t),str(answer))