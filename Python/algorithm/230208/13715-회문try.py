#찾을 스트링 만들기 -> M인 스트링 만들기 -> 반잘라서 앞뒤 비교 -> 같으면 스트링 리턴하기.
# 아 근데 굳이 반 안잘라도 되네... 그냥 다 돌리면 되네........................ 빡대갈이다...
# https://totoma3.tistory.com/124
T = int(input())
for tc in range(1, T+1):
    N,M=map(int, input().split()) #N개의 글자를 가짐, 길이가 M인 회문 찾기
    ans = ' '
    strs = [input() for _ in range(N)] #1차원 배열

    ans = ''
    #가로 확인
    for i in strs:
        str1, str2 = '', ''
        for j in range(len(i)-M+1):
            str1=i[j:j+M//2]
            str2=i[j+M//2:j+M]
            # print(str1, str2)
            # print(str2[1:][::-1])
            if M % 2 == 0:  # 길이가 짝수면 반반 그냥 더하면 됨
                if str1==str2[::-1]:
                    ans = str1 + str2
            else:
                if str1==str2[1:][::-1]: # 길이가 홀수면 중간 애도 더해 줘야 됨
                    ans = str1 + str2

    # ans가 안 나왔으면 세로 확인:
    if ans=='':
        newstr = []
        for k in range(len(strs)):
            n = ''
            for l in range(len(strs)):
                n+=strs[l][k]
            newstr.append(n)
        for i in newstr:
            str1, str2 = '', ''
            for j in range(j, len(i)-M+1):
                str1 = i[j:j + M // 2]
                str2 = i[j + M // 2:j + M]
                if M % 2 == 0:  # 길이가 짝수면 반반 그냥 더하면 됨
                    if str1 == str2[::-1]:
                        ans = str1 + str2
                else:
                    if str1 == str2[1:][::-1]:  # 길이가 홀수면 중간 애도 더해 줘야 됨
                        ans = str1 + str2

    print(f'#{tc} {ans}')





    #
    #
    # #가로 스트링
    # for i in strs:
    #
    # for i in strs: #가로 확인
    #     start = 0
    #     str1,str2,str3 = '','',''
    #     for j in range(0, len(i)-M+1): #전체길이-길이M인회문 동안
    #         for k in range(start, M//2): #비교할 문자열 만들기 (기준:M)
    #             str1+=i[k] #앞에서부터
    #             str2+=i[-(k+M//2+1)] #뒤에서부터
    #             str3 = i[k+1]
    #         print(str1, str2)
    #         if str1 == str2:
    #             if M % 2 == 0:  # 길이가 짝수면 반반 그냥 더하면 됨
    #                 ans = str1 + str2[::-1]
    #             else:  # 길이가 홀수면 중간 애도 더해 줘야 됨
    #                 ans = str1 + str3 + str2[::-1]
    #         start += 1
    #
    # if ans == ' ': #가로에서 못 찾았으면 세로 확인
    #     for a in range(len(strs)):
    #         pass



    # 아주 기초문제로생각햇던..
    # if len(strs) == M:  # 가로로 찾기
    #     str1 = strs[:len(strs) // 2]
    #     str2 = strs[-len(strs) // 2::]
    #     if str1 == str2[::-1]:
    #         ans = strs