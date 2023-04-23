# 1460. 데일리과제 7-4. 객체지향 프로그래밍의 이해와 기

def collatz(num):
    count = 0

    while(num>1):
        if num%2==0:
            num /=2
            count+=1
        else: 
            num = num*3+1
            count+=1
        if count>=500:
            count=-1
            break
    return print(count)

collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
