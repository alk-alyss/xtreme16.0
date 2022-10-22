mod = 10**9+7
N, workers = list(map(int, input().split()))
tasks = list(map(int, input().split()))
tasks.sort(reverse=True)

# big = tasks[0]
# days = big
# i = 1
# s = big - max(tasks[i:i+workers-1])
# if s > 0:
#     i += workers-1
# else:
#     big = tasks[i+workers]
#     days += big

totalTime = 0
runningTasks = []
start = 0
while len(tasks) > 0:
    end = start + workers
    runningTasks.extend(tasks[start:end])

    start += workers
    workers = 0

    time = min(runningTasks)
    totalTime += time
    i = len(runningTasks)
    while i > 0:
        task = runningTasks[i]
        task -= time
        if task == 0:
            runningTasks.pop(i)
            workers += 1
        i -= 1

print(totalTime)
