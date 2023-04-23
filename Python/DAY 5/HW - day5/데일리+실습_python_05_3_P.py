# 입력 예시
# s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'


s = input()
s=s.strip('@#~!>"$%()*+,-/:;<=?[]\^_`{|}')

inum=s.find('I')
news=''
if inum!=-1:
    news+=s[:inum].lower()
    news+=s[inum]
    news+=s[inum+1:].lower()
else: news=s.lower()

print(news)


# 생각: 아스키코드 써서 문자(. 제외) 살리고 앞뒤 다 삭제.
#ㄴㄴ 걍 strip 쓸래.......
# find 써서 I 찾고 앞뒤 다 lower ㅋㅋ