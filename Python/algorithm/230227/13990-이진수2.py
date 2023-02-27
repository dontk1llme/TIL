# [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 (제출용) D2

T = int(input())
for tc in range(1, T+1):
    n = float(input())
    lst = []
    while n>0:
        if len(lst)>12:
            # print(f'#{tc} {"overflow"}') #이렇게 하면 두번 출력됨
            lst = ['overflow']
            break
        lst.append(int(n//2**(-1*len(lst)-1))) #마지막 -1 주의
        n %=(2**(-1*len(lst)))

    ans = ''.join(map(str,lst)) #int는 join 안됨
    print(f'#{tc} {ans}')

#///////////////////////////////
ip = int(input())

for case in range(1, ip + 1):
    n = float(input())
    ans = ''
    cnt = 1
    while n and cnt < 13:
        if n >= 2 ** (-cnt):
            n -= 2 ** (-cnt)
            ans += '1'
        else:
            ans += '0'
        cnt += 1

    if n:
        print(f'#{case} overflow')
    else:
        print(f'#{case} {ans}')