# [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 (제출용) D2

T = int(input())
for tc in range(1,T+1):
    s = input()
    stk=[]
    tmp = ''
    for i in range(len(s)):
        # if s[i] == tmp: #연속문자 다 지우는줄 알았는데 두개씩만 지우네...
        #     pass
        if len(stk)==0:
            stk.append(s[i])
        elif s[i]==stk[-1]:
            tmp = stk[-1]
            stk.pop()
        else: stk.append(s[i])

    # print(stk)
    print(f'#{tc} {len(stk)}')