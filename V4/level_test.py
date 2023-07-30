import Karakter

base_xp = 100
n1 = 1.25

for level in range(0, 10):
    print(int(base_xp *(n1**level)))
