#연속한 1의 개수 찾기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = int(input(), 16) #10진수로 입력받기

    #2진수로 변환
    num2 = ''
    while num>0:
        num2+=str(num%2)
        num=num//2
    num2 = num2[::-1]
    num2+='0' #아래 else조건 만족시켜주려고 무조건 예외 만들기

    #연속하는 1의 최대 개수 구하기
    ans = 0
    tmp = 0
    for i in range(1, len(num2)):
        if num2[i]=='1':
            if num2[i]==num2[i-1]:
                tmp+=1
        else:
            ans = max(ans, tmp)
            tmp=0

    if ans!=0:
        ans+=1
    print(f'#{tc} {ans}')