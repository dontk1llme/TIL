#  [파이썬 S/W 문제해결 기본] 5일차 - Forth (제출용) D2
# 예외처리 중요...
# stk이 비었는데 연산하라고 함->에러 >>생각함
# 연산 완료했는데 stk에 남은 게 2개 이상 -> 에러 >> 얘 생각을 안햇음

T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())
    stk = []
    ans=True
    # print(lst)

    for i in range(len(lst)-1):
        if lst[i].isdigit():
            stk.append(int(lst[i]))

        else:
            try:
                # if len(stk)>=2: #스택에 숫자가 무조건 두 개 이상 있어야 연산 가능
                num2 = stk.pop()
                num1 = stk.pop()
                if lst[i] == '+':
                    stk.append(num1+num2)
                elif lst[i]=='*':
                    stk.append(num1*num2)
                elif lst[i]=='/':
                    stk.append(num1//num2) #// 안 하면 틀렷다함...;
                elif lst[i]=='-':
                    stk.append(num1-num2)
            except:       #숫자 2개 미만일 때 연산하라고 하면 올바르지 않은 식이라 error
                ans=False
    if ans==False or len(stk)!=1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stk.pop()}')


