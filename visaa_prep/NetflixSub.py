P, Q, R, a = map(int,input().split())

if P+Q >= a or P+R >= a or Q+R >= a:
    print("YES")

else:
    print("NO")
