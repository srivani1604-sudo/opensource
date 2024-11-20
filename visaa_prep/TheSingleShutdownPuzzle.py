n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
z_r=set()
z_c=set()
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            z_r.add(i)
            z_c.add(j)
for i in range(n):
    for j in range(m):
        if i in z_r or j in z_c:
            a[i][j]=0
for i in a:
    print(" ".join(map(str,i)))
