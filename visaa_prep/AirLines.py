a,b=map(int,input().split())
m=b-a*100
a1=m/100
a2=m//100
if a1-a2>0:
    print(a2+1)
else:
    print(a2)
