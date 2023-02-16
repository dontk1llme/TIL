# [BOJ] 9251 LCS
# 첨에는 부분집합 생각함. 근데 그게 그거임.
# DP 사용해야 함. 하나하나->큰거 봐야하니까.
# 엑셀처럼?? 겹치는 부분 세면 되는 거 아님?
# -> 2차원배열 만들어서
# 이해안됨....................................
# 알고리즘
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
# 문제풀이
# https://bgspro.tistory.com/134 표 참고해서 이해하세요
# https://haerang94.tistory.com/184
# https://hibee.tistory.com/241

s1 = input() # 기준
s2 = input() # 하나씩 증가시키며 비교할것
lst = [list([0]*(len(s2)+1)) for _ in range(len(s1)+1)] #인덱스 편하게 하려고 하나씩 늘려줌 (블로그에서 착안)
# print(lst)

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            lst[i][j]+=lst[i-1][j-1]+1
        else:
            lst[i][j] = max(lst[i-1][j], lst[i][j-1])
print(lst[-1][-1])


