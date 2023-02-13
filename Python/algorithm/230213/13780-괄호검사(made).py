# Stack1_연습문제_1: 괄호검사 (제출용) D1

T = int(input())

for tc in range(1,T+1):
    s = list(map(str, input()))
    stk = []
    ans = 0
    for i in range(len(s)):
        if s[i]=='(':
            stk.append(s[i])
        elif s[i]==')':
            if len(stk)==0:
                stk.append('-') #스택이 비었을 경우 답을 1로 햇는데 그냥 break하면 여전히 빈 스택이라서 아무거나 넣어줌
                break
            stk.pop()
    if len(stk)==0:
        ans =1
    print(f'#{tc} {ans}')

