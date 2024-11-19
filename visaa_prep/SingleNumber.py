n=int(input())
m=list(map(int,input().split()))
for i in m:
    if m.count(i)==1:
        print(i)
