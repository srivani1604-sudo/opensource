A, B, C = map(int, input().split())
max_weight = C-B
if max_weight <= 0:
    print(0)
else:
    max_mangoes = max_weight // A
    print(max_mangoes)
