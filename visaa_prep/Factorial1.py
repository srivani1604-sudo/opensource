def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input())
if 1 <= n <= 15:
    print(factorial(n))
else:
    print("Please enter a number between 1 and 15")
