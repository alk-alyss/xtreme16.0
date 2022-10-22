N, M = list(map(int, input().split()))
tasks = sorted(list(map(int, input().split())), reverse=True)
if (M > 1): print(2**tasks[0]%(10**9+7))
else: print(sum([2**task for task in tasks])%(10**9+7))
