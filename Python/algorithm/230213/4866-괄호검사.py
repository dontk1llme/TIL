# 4866 [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사 (제출용) D2.
#break warning............

T = int(input())
for tc in range(1, T+1):
    s = input()

    stk = []
    ans = 1
    for i in range(len(s)):
        if s[i]=='{' or s[i]=='(':
            stk.append(s[i])
        elif s[i]=='}' or s[i]==')':
            if len(stk)==0:
                ans=0
                break
            elif s[i]=='}':
                if stk[-1]=='{':
                    stk.pop()
                else:
                    ans = 0
                    break
            elif s[i]==')':
                if stk[-1]=='(':
                    stk.pop()
                else:
                    ans = 0
                    break

    if len(stk)!=0:
        ans=0
    print(f'#{tc} {ans}')
