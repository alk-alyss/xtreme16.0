T = int(input())
output = []
for _ in range(T):
    dim = input().split(" ")
    N, M, D = dim
    N = int(N)
    M = int(M)
    D = int(D)
    design = []
    inputIndex = set()
    outputIndex = set()
    for _ in range(D):
        design.append([])
        for _ in range(N):
            design[-1].extend(input().strip().split(" "))
        input()
