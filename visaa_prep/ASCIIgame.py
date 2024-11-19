s=input()
p=""
for i in s:
    if i.isupper():
        p+=i.lower()
    if i.islower():
        p+=i.upper()
print(p)
