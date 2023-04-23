# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(ls):
    ls.sort()
    newls = list(set(ls))
    newls.sort()
    count=[0]*len(newls)

    for i in ls:
        for j in range(0,len(newls)):
            if i == newls[j]:
                count[j]+=1
    sum=0
    for i in range(0,len(count)):
        if count[i]==1: sum+=newls[i]
    print(sum)

if __name__=="__main__":
    ls = list(map(int, input().split(', ')))
    sum_of_repeat_number(ls)
    

