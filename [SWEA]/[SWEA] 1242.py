#  [S/W 문제해결 응용] 1일차 - 암호코드 스캔 (제출용) D5
# 중복 제거해서 입력받고 0만 있는 열 없애기
# 16진수->2진수
# 왼쪽 0 다 제거
# 마지막에 0 붙임

ratio = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split()) #세로 n 가로 m
    lst = list(set([input()for _ in range(n)])) #중복 제거해서 입력받기
    lst = sorted(lst)[1:] #0만 있는 애가 맨 앞에 오니까 걔 뺌

    numbers = [] #암호
    ans = 0
    for l in lst:
        binary = format(int(l,16),'b').lstrip('0')+'0'
        n1,n2,n3=0,0,0
        cnt = 0  # 암호 8자리
        odd = 0  # 홀수 자리 합 저장
        even = 0  # 짝수 자리 합 저장
        tmp  = ''
        for i in range(len(binary)):
            if binary[i] == '1' and n2 == 0:  # 첫번째 1 비율
                n1 += 1
            elif binary[i] == '0' and n1 != 0 and n3 == 0:  # 두번째 0 비율
                n2 += 1
            elif binary[i] == '1' and n2 != 0:  # 세번째 1 비율
                n3 += 1
            elif n3 != 0:  # 비율 다 구한 경우
                cnt += 1
                r = min(n1, n2, n3)  # 가장 작은 숫자 구하기 (비율 구하기 위함)
                pw = ratio[(n1 // r, n2 // r, n3 // r)]  # 암호 가져오기
                tmp += str(pw)
                # 마지막 번호인 경우
                if cnt == 8:
                    if (odd * 3 + even + pw) % 10 == 0 and tmp not in numbers:  # 정상적인 암호코드이고 했던거 아니라면
                        ans += odd + even + pw  # 값 더해주기
                    numbers.append(tmp)  # 해당 암호 저장
                    odd = even = cnt = 0  # 변수들 초기화
                    tmp = ''
                # 8번째 자리 이전의 숫자인 경우
                elif cnt % 2:
                    odd += pw  # 홀수 자리 더하기
                else:
                    even += pw  # 짝수 자리 더하기

                n1 = n2 = n3 = 0  # 비율 변수 초기화

    print(f'#{tc} {ans}')
