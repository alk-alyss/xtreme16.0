

t = int(input())
output = []
for _ in range(t):
    price = 0
    s, c, r = list(map(int, input().split()))
    curTank = c
    price += c * r
    # print(price)
    path = []
    for station in range(s):
        liters, cost = list(map(int, input().split()))
        path.append((liters, cost))
    willRefill = None
    for i in range(len(path)-1):
        curTank -= path[i][0]
        if willRefill == None:
            canTravel = []
            tempTank = curTank
            for j in range(i+1, len(path)):
                if tempTank >= path[j][0]:
                    canTravel.append((j, path[j][1]))
                    tempTank -= path[j][0]
            possibleReffils = [(i, path[i][1])]
            possibleReffils.extend(canTravel)
            possibleReffils = sorted(possibleReffils, key=lambda x: x[1])
            willRefill = possibleReffils[0][0]
        if willRefill == i and willRefill != len(path)-1:
            price += (c - curTank) * path[i][1]
            price += 500
            curTank = c
            willRefill = None
    output.append(price)

for o in output:
    print(o)
