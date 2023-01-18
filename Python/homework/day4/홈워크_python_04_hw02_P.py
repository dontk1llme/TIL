#2218. 데일리과제 4-4. 문자열 애너그램 예제 Lv4

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

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
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    group_anagrams(words)
