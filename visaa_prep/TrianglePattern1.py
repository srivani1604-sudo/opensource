N = int(input())
num = 1
for i in range(1, N + 1):
    print(" ".join(str(num + j) for j in range(i)))
    num += i
