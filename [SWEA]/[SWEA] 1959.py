#[SWEA] 1959 두 개의 숫자열 D2

time = int(input())
for t in range(1, time+1):
    n, m = map(int,(input().split()))
    
    # 번거롭게 곱하기 식 두 번 쓰려고 했는데 그럴 바에 처음부터 길이에 따라 경우 나눠서 입력받고
    # 계산식을 한번에 하는 게 훨씬 편안할 것 같음.
    if n>m:
        big=n
        small=m
        a = list(map(int,(input().split())))
        b = list(map(int,(input().split()))) 
    else: 
        big=m
        small=n
        b = list(map(int,(input().split())))
        a = list(map(int,(input().split())))
    
    max=0
    for i in range(big-small+1):
        sum = 0
        for j in range(small):
            sum += b[j]*a[j+i] #이 식 이해좀...
        if sum>max:
            max=sum
    print(f'#{t} {max}')


    


