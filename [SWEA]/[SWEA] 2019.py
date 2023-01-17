#swea 2019. 더블더블 D1
num = int(input())
x = 1
for i in range(0,num+1):
    if i==0: print(x, end=' ')
    else: 
        x = x*2
        print(x, end=' ')