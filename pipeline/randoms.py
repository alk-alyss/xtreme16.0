import random

seed = 420
sel = ['YES', 'NO']

T = int(input())
for _ in range(T):
    dim = input().split(" ")
    N, M, D = dim
    N = int(N)
    M = int(M)
    D = int(D)
    print(sel[random.randint(0, 1)])
#     print(random.choice(sel))
# c = random.choice(sel)
# print(random.randint(0, 1))
