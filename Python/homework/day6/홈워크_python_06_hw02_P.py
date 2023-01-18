#1453. 데일리과제 6-4. 데이터 구조 복습 및 심화 예제2

# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']
# eat, tea, tan, ate, nat, bat

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

def group_anagrams(my_list):
    newlist=[] #출력용으로 저장할 리스트
    sortlist=[] #이름 바꿔서 저장...

    # 정렬해서 sortlist에 저장
    for i in range(0,len(my_list)):
        sortlist.append(''.join(sorted(my_list[i])))
    ss1 = list(set(sortlist)) #몰아넣기
    
    for i in range(0,len(ss1)):
        same=[]
        for j in range(0,len(my_list)):
            
            if ss1[i]==sortlist[j]:
                same.append(my_list[j])
            else: pass
                
        newlist.append(same)    
    print(newlist)
    

if __name__=="__main__":
    my_list=list(input().split(', '))    
    group_anagrams(my_list)


'''시간 1시간 넘게 걸림.
생각한 방법 
1: dict를 만들어서 {원래단어:정렬단어} 해서 정렬단어끼리 비교한 후 원래단어를 리스트에 추가하려고 했음
    생각해보니 dict는 indexing이 안 돼서 포기
2: dict를 분해한 리스트 두 개를 만들어서 사용하려고 했음. 근데 list in list 형식으로 만드는 데 한계가 생김
3: 그래서 set를 이용해서 정렬단어만 있는 리스트를 생성함. 얘랑 비교해서 list in list 생성
etc: 변수 이름 좀 잘 지어라 중복 하지 말고...
'''