# swea 5432. 쇠막대기 자르기 D4

# ( 개수 세고 있다가... count+=1
# () 나오면 쇠막대기 컷! ans+=count
# ) 나오면 ans+1 해주고 count-=1
# 스택 쓰자 스택

T = int(input())
for tc in range(1, T+1):
    s = input() #레이저: (), 쇠막대기 끝: (, )

    ans=0
    count=0
    iron=[]
    i=0

    while i<len(s):
        if s[i]=='(':
            if i<len(s) and s[i+1]==')':
                ans+=count
                i+=2
            else:
                iron.append(s[i])
                count+=1
                i+=1

        elif s[i]==')':
            iron.pop()
            ans+=1
            count-=1
            i+=1

    print(f'#{tc} {ans}')

