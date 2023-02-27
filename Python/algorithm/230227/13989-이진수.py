#  [파이썬 S/W 문제해결 구현] 1일차 - 이진수 (제출용) D2
# https://codingpractices.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2%EC%A7%84%EC%88%98-8%EC%A7%84%EC%88%98-10%EC%A7%84%EC%88%98-16%EC%A7%84%EC%88%98-%EB%B3%80%ED%99%98-%EC%B4%9D%EC%A0%95%EB%A6%AC-bin-oct-hex-str-format-%EC%9D%B4%EC%9A%A9



T = int(input())
for tc in range(1,T+1):
    N, num = input().split()
    ls = []
    for i in num:
        n = int("0x"+i, 16) #0x: 16진수
        # print(f'{n:04b}')
        ls.append(f'{n:04b}') #이건뭐냐? 04b?
    ans = ''.join(ls)
    print(f'#{tc} {ans}')

