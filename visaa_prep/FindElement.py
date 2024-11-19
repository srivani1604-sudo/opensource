n=int(input())
a=list(map(int,input().split()))
m=int(input())
if m in a:
    print(a.index(m))
else:
    print(-1)
