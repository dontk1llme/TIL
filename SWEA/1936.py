#SWEA 1936 #1대1 가위바위보

a,b = map(int,input().split())

win =[0,3,1,2]
if a==b:
    print("비김")
elif win[a]==b:
    print("A")
else: print("B")