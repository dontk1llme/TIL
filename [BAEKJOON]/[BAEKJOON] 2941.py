# [BAEKJOON] 2941 크로아티아 알파벳
#replace!!!!!!!!!!생각!!!!!!!!!!!!!!!!!!!!!!!! 개열박ㄷ내

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))

#/////////////////////////////////////////////////////////////////
cr =['c=','c-','dz=','d-','lj','nj','s=','z=']

s = input()
i = 0
cnt=0
out=True
while out:
    for l in cr:
        i = s.find(l)
        if i!=-1:
            s = s[:i]+s[i+len(l):]
            cnt+=1
            print(s)
            break
        else:
            if l=='z=':
                out=False
cnt+=len(s)
print(cnt)


