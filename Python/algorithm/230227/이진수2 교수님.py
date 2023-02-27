T = int(input())
for tc in range(1, T + 1):
    f = float(input())
    ans = ''
    while f > 0.0:  # 곱한 값이 0이 아닌동안 계속 변환
        f *= 2
        if f >= 1.0:  # 정수 부분 '1'을 저장
            ans += '1'
            f -= 1.0
        else:
            ans += '0'
        if len(ans) > 12:
            ans = 'overflow'
            break

    print(f'#{tc} {ans}')