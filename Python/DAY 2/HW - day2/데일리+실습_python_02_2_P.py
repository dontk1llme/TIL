# 1674. 데일리실습 2-2. 문자열 메소드 이해 및 문재 해결 
'''HTML 문서의 text 양옆에는 태그가 있다. HTML text를 입력받아 P 태그를 지우고 나머지 text를 출력하라.
문자열 <code>slicing</code>을 이용하라
P 태그는 <code><p></code>와 <code></p></code>이다.'''

# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

html=input()
l,r=0,0
for i in range(1,len(html)-1):
    if html[i]=='>': l=i
    elif html[i]=='<': r=i
print(html[l+1:r])

