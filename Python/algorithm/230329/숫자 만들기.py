#  [모의 SW 역량테스트] 숫자 만들기 (제출용) D4

T = int(input())

def calculate(a,b,c):
    # global cnt
    # cnt+=1
    if c==0:
        return a+b
    elif c==1:
        return a-b
    elif c==2:
        return a*b
    else: return int(a/b) #나머지 버림

def dfs(idx, ans):
    # num은 그대로, cal만 조합해보기
    global minn, maxx
    if idx>=N:
        if ans>maxx:
            maxx=ans
        if ans<minn:
            minn=ans
        return

    for i in range(4): #이걸 못짰어..
        if cal[i]:
            cal[i]-=1
            dfs(idx+1, calculate(ans,num[idx+1],i))
            cal[i]+=1

for tc in range(1, T+1):
    N = int(input())-1 #-1 꼬옥 해줘야함... 숫자들 사이에만 연산자가 들어가니까 . .
    cal = list(map(int, input().split())) # + - * /
    num = list(map(int, input().split()))
    cnt = 0

    minn = 100000000
    maxx = -100000000

    dfs(0, num[0])
    # print(cnt)
    print(f'#{tc} {maxx-minn}')
