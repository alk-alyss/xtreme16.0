mod = 10**9+7
N, M = list(map(int, input().split()))
tasks = list(map(int, input().split()))
if (M > 1): print(2**max(tasks)%mod)
else: print(sum([(1 << task)%mod for task in tasks])%mod)
