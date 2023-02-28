# Start_연습문제_3_암호 출력 (제출용) D2
#변수명 겹치게주면 닌진짜뒤진다

bitdic = {'001101':'0', '010011':'1', '111011':'2', '110001':'3', '100011':'4',
       '110111':'5', '001011':'6', '111101':'7', '011001':'8', '101111':'9' }

T = int(input())
for tc in range(1, T+1):
    lst = input()

    #이진수 변환
    bitlst = []
    for x in lst:
        n = int(x,16)
        for j in range(3,-1,-1):
            bit = '1' if n&(1<<j) else '0'
            bitlst.append(bit)

    bitnum=''.join(bitlst)

    #암호 변환
    print(f'#{tc}', end=' ')
    start=0
    while start<len(bitnum)-5:
        if bitnum[start:start+6] in bitdic:
            print(bitdic[bitnum[start:start+6]], end=' ')
            start+=5
        start+=1
    print('')
