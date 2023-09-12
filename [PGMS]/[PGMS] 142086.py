# pgms 142086 가장 가까운 같은 글자
# lv1, 30min

def solution(s):
    answer = [-1]*len(s)
    
    for i in range(0,len(s)):
        n = 0
        for j in range(i-1,-1,-1):
            if s[i]==s[j]:
                print(i,j)
                n = i-j
                break
        if n!=0:
            answer[i]=n
        
    return answer