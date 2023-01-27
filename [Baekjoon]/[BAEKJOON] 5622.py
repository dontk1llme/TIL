#[BAEKJOON] 5622. 다이얼 (자료구조 때 실패했던 거 2년 만에 도전...)
#개쉽노..;

dial = input()
num=[]
sec=0
for i in dial:
    if i == 'A' or i=='B' or i=='C': 
        num.append('2')
        sec+=3
    elif i == 'D' or i=='E' or i=='F': 
        num.append('3')
        sec+=4
    elif i == 'G' or i=='H' or i=='I': 
        num.append('4')
        sec+=5
    elif i == 'J' or i=='K' or i=='L': 
        num.append('5')
        sec+=6
    elif i == 'M' or i=='N' or i=='O': 
        num.append('6')
        sec+=7
    elif i == 'P' or i=='Q' or i=='R' or i=='S': 
        num.append('7')
        sec+=8
    elif i == 'T' or i=='U' or i=='V': 
        num.append('8')
        sec+=9
    elif i=='W' or i=='X' or i=='Y' or i=='Z':
        num.append('9')
        sec+=10

print(sec)