def finding_max(ls, h):
    mx = ls[0]
    # pos = 0
    mn = min(A)
    for i in range(1, len(ls) - 1):

        if ls[i - 1] < ls[i] and ls[i] > ls[i + 1]:
            # print(ls[i])
            print(ls[i], mx)
            if mx < ls[i] and ls[i] - mn == h:
                # pos = i
                mx = ls[i]
    if ls[-1] > ls[-2] and ls[-1] > mx:
        mx = ls[-1]
    return mx


m, n, t = list(map(int, input().split()))

if m == 1:
    A = list(map(int, input().split()))

# print(A)
print(finding_max(A, t))
