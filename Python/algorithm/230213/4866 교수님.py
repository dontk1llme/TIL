#1
dct = {'{': '}', '(': ')'}
T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []
    ans = 1
    # 대상 괄호문자를 제외한 나머지는 아무 동작하지 않음
    for ch in st:
        # 열리는 괄호인 경우: 닫히는 괄호를 push
        if ch in dct:  # dct의 key값 중에 있는 경우
            stk.append(dct[ch])  # 나중 비교할때 간단하게 하기위해 쌍이 되는 문자를 push
        elif ch in dct.values():
            try:
                if ch != stk.pop():
                    ans = 0
                    break
            except:  # stk empty로 pop동작 오류
                ans = 0
                break

            # if not stk or ch != stk.pop():
            #     ans = 0
            #     break
    if stk:  # 모든 처리후 스택에 데이터 있으면 괄호 오류
        ans = 0
    print(f'#{test_case} {ans}')

#2
dct = {'{':'}', '(':')'}
T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []
    ans = 1
    # 대상 괄호문자를 제외한 나머지는 아무 동작하지 않음
    for ch in st:
        # 열리는 괄호인 경우: 닫히는 괄호를 push
        if ch in dct:           # dct의 key값 중에 있는 경우
            stk.append(dct[ch]) # 나중 비교할때 간단하게 하기위해 쌍이 되는 문자를 push
        elif ch in dct.values():
            if not stk or ch != stk.pop():
                ans = 0
                break
    if stk:     # 모든 처리후 스택에 데이터 있으면 괄호 오류
        ans = 0
    print(f'#{test_case} {ans}')
