# 1449. 데일리실습 6-3. 크롤링을 통한 서비스 개발

def count_vowels(str):
    str = str.lower()
    count=0
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    print(count)

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3