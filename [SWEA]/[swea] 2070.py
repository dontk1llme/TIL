# 2070. 큰 놈, 작은 놈, 같은 놈 D1

num = int(input())

for i in range(num):
    x,y = map(int, input().split())
    if x > y:
        print("#"+str(i+1),">")
    elif x == y:
        print("#"+str(i+1),"=")
    else: print("#"+str(i+1),"<")
    
#map문 for 안에 넣어야 하는 거 까먹음... ;;