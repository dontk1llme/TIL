# 4949. 균형잡힌 세상
# [], ()
# stack 사용
#break 사용 주의

while True:
    strr = input()
    if strr=='.': #입력받으면 종료
        break
    
    stk =[]
    for i in strr:
        if i=='(' or i=='[':
            stk.append(i)
        elif i==')':
            if len(stk)!=0 and stk[-1]=='(':
                stk.pop() #마지막 요소 삭제
            else: 
                stk.append(i)
                break
        elif i==']':
            if len(stk)!=0 and stk[-1]=='[':
                stk.pop() #마지막 요소 삭제
            else: 
                stk.append(i)
                break 
    if len(stk)==0:
        print('yes')
    else: print('no')




