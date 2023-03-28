# 10804. 문자열의 거울상 D3
T = int(input())
for tc in range(1, T+1):
    strs = input()
    ans = ''
    strs = strs[::-1]
    #거울을 옆에서 비춘다고 생각해야...
    for i in range(len(strs)):
        if strs[i] == 'b':
            ans+='d'
        elif strs[i] == 'd':
            ans+='b'
        elif strs[i] == 'p':
            ans+='q'
        elif strs[i]=='q':
            ans+='p'


    print(f'#{tc} {ans}')

    # 거울을 아래서 비추면...
    # for i in range(len(strs)):
    #     if strs[i] == 'b':
    #         ans+='p'
    #     elif strs[i] == 'd':
    #         ans+='q'
    #     elif strs[i] == 'p':
    #         ans+='b'
    #     elif strs[i]=='q':
    #         ans+='d' 
 
