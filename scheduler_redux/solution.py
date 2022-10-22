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
doneTasks = 0
while doneTasks < len(tasks):
    end = start + workers
    newTasks = [pow(2, task, mod) for task in tasks[start:end]]
    runningTasks.extend(newTasks)

    start = end
    workers = 0

    time = min(runningTasks)
    totalTime += time
    i = len(runningTasks)-1
    while i >= 0:
        runningTasks[i] -= time
        if runningTasks[i] == 0:
            runningTasks.pop(i)
            doneTasks += 1
            workers += 1

        i -= 1

print(totalTime%mod)
