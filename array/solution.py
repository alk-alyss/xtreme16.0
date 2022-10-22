def getSolution(l, r, k, p):
    global array







n, m, p = list(map(int, input().split()))

array = [0 for _ in range(n)]

for _ in range(m):
    l, r, k = list(map(int, input().split()))
    l -= 1
    l -= 1

    for i in range(l, r):
        array[i] += 1

print(array)
