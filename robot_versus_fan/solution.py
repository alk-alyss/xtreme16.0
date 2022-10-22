def convertRobotSteps(steps):
    convertedSteps = {}

    robot = [0,0]

    while True:
        step = steps[robot[0]][robot[1]]

        nextRobot = [robot[0], robot[1]]

        if step == ">":
            nextRobot[1] += 1
        elif step == "<":
            nextRobot[1] -= 1
        elif step == "^":
            nextRobot[0] -= 1
        elif step == "v":
            nextRobot[0] += 1

        robotTuple = tuple(robot)
        nextRobotTuple = tuple(nextRobot)

        convertedSteps[robotTuple] = nextRobotTuple

        if nextRobotTuple in convertedSteps:
            break

        robot = nextRobot

    return convertedSteps

def simulate(robot, dust):
    i = 0
    maxI = -1

    lenRobotLoop = len(set(robot.values()))
    lenDustLoop = len(dust)
    if lenRobotLoop > lenDustLoop:
        if lenRobotLoop % lenDustLoop == 0:
            maxI = lenRobotLoop
    else:
        if lenDustLoop % lenRobotLoop == 0:
            maxI = lenDustLoop

    currentRobot = (0,0)

    while True:
        if i == maxI:
            return "never"

        currentDust = dust[i%len(dust)]

        if currentRobot == currentDust:
            return i

        currentRobot = robot[currentRobot]

        i += 1


T = int(input())

for _ in range(T):
    r = int(input())

    robotMovements = []

    for _ in range(r):
        robotMovements.append(input())

    d = int(input())

    dustSteps = []

    for _ in range(d):
        dustSteps.append(tuple(map(int, input().split())))

    robotSteps = convertRobotSteps(robotMovements)

    commonSteps = set(robotSteps.keys()).intersection(set(dustSteps))

    if len(commonSteps) == 0:
        print("never")
        continue

    result = simulate(robotSteps, dustSteps)

    print(result)
