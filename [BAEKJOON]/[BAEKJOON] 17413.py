# [BAEKJOON] 17413 단어 뒤집기 2

s = input()
idx = 0
rev = ''
while idx < len(s):
    if s[idx]=='<': #괄호 안의 내용들 다 순서대로 출력
        while s[idx]!='>':
            print(s[idx], end='')
            idx+=1
            if idx==len(s):
                break
        print(s[idx], end='') #>
        idx+=1
    elif s[idx]==' ': #공백이면 그냥 출력
        print(s[idx], end='')
        idx+=1
    else: #뒤집어야 하는 부분만 따로 만들어서 출력
        while s[idx]!='<' and s[idx]!=' ':
            rev+=s[idx]
            idx+=1
            if idx==len(s):
                break
        print(rev[::-1], end='')
        rev = ''



