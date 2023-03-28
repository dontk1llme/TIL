# SWEA 4366  정식이의 은행업무 (제출용) D4
#완전탐색, https://epser.tistory.com/19
# https://wizdom.tistory.com/217

T = int(input())
for tc in range(1, T+1):
    two=input()
    three=input()
    tmp = []
    for i in range(len(two)): #0이면 1로, 1이면 0으로 바꿈 -> 10진수로 -> tmp에 저장함
        if two[i]=='0':
            change = two[:i]+'1'+two[i+1:]
            tmp.append(int(change,2))
        else:
            change = two[:i]+'0'+two[i+1:]
            tmp.append(int(change, 2))

    ter = '012'
    for i in range(len(three)):
        for j in ter:
            if three[i]==j: #원래 숫자랑 같으면 넘어가기
                continue
            #해당 자리 숫자 바꿔서 10진수로 변환
            change = int(three[:i] + j + three[i+1:], 3)
            if change in tmp: #변환한 수가 2진수로 만든 수 중에 잇으면
                print(f'#{tc} {change}')
                break



