# 1446. 데일리과제 5-4. 셀프넘버 및 제너레이터 찾기 예제 lv4

# fn_d(91) 
# 출력 예시 
# 101

def fn_d(gen):
    sgen = str(gen)
    n = gen
    for i in range(0,len(sgen)):
        n += int(sgen[i])
    return n


def is_selfsumber(n):
    count=0
    ls = []
    for i in range(0,n):
        if fn_d(i) ==n: 
            count+=1
            ls.append(i)
    if count==0: print("셀프넘버이다.")
    else: print(f'{n}의 제너레이터는 {count}개이며 목록은 다음과 같다. \n목록: {ls}')



            
    
    