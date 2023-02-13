T = int(input())
for test_case in range(1, T + 1):
    st = input()
    stk = []
    for ch in st:
        if not stk:  # 스택 emptt => 무조건 push
            stk.append(ch)
        else:
            if ch == stk[-1]:  # 반복문자
                stk.pop()
            else:
                stk.append(ch)

    print(f'#{test_case} {len(stk)}')