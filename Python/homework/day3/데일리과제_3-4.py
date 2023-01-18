# 2216. 데일리과제 3-4. 삼각형 종류 판별하기

s_triangle = list(map(int, input().split()))
s_triangle.sort() #할당해 주지 않아도 정렬되어 저장!

if s_triangle[0]+s_triangle[1]>s_triangle[2]: #삼각형인지 아닌지부터 판별
    if s_triangle[0]==s_triangle[1]==s_triangle[2]:
        print("정삼각형")
    elif s_triangle[0]==s_triangle[1] or s_triangle[1]==s_triangle[2] or s_triangle[2]==s_triangle[0]:
        print('이등변삼각형')
    elif s_triangle[0]**2+s_triangle[1]**2==s_triangle[2]**2:
        print('직각삼각형')
    else: print('삼각형')
else: print('삼각형 아님')
