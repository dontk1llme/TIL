T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []
    ans = 1

    for ch in st:  # 입력 문자열을 하나씩 처리
        if ch == '(':  # push
            stk.append(ch)
        else:
            if stk:  # stk pop전에 반드시 if stk (stk에 데이터 있는지 체크)
                stk.pop()
            else:  # pop해야 하는 상황인데 stk empyt! ==> 에러
                ans = 0
                break

    # 모든 처리 완료후 stk에 데이터가 남았다면.. 오류
    if stk:  # ')' 괄호 부족
        ans = 0
    print(f'#{test_case} {ans}')