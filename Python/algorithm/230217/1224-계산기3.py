
T = 10
for tc in range(1,T+1):
    N = int(input())
    cal = input()

    #후위표기로 만들기
    stk = [] #연산자 스택
    lst = [] #후위표기식
    prior = {'*':2, '/':2, '+':1, '-':1, '(':0}
    for i in range(len(cal)):
        if cal[i].isdigit():
            lst.append(cal[i])
        elif cal[i]=='(':
            stk.append(cal[i]) # ( 넣기
        elif cal[i]==')':
            while stk[-1]!='(':
                lst.append(stk.pop())
            stk.pop() # ( 없애기
        else: #괄호 이외의 연산자
            while stk and prior[cal[i]] <= prior[stk[-1]]:
                lst.append(stk.pop())
            stk.append(cal[i])
    while stk:
        lst.append(stk.pop())  #남아있는 연산자들 처리...

    num = []
    for i in lst:
        if i.isdigit():
            num.append(int(i))
        else:
            if len(num)>=2:
                num2 = num.pop()
                num1 = num.pop()
                if i=='+':
                    num.append(num1+num2)
                elif i=='*':
                    num.append(num1*num2)
                elif i=='/':
                    num.append(num1//num2)
                elif i=='-':
                    num.append(num1-num2)
    print(f'#{tc} {num[0]}')

