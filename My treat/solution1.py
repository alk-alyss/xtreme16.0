from collections import defaultdict


T = int(input())

output = []
for _ in range(T):
    paid = defaultdict(list)
    ate = defaultdict(list)
    M = int(input())
    for _ in range(M):
        meal = input().split()
        paid[meal[0]].append(int(meal[1]))
        for i in range(2, 2 + int(meal[1])):
            ate[meal[i]].append(1)
    for person in paid:
        paid[person] = sum(paid[person])
    for person in ate:
        ate[person] = sum(ate[person])
    personAte = list(ate.keys())
    for person in personAte:
        if person in paid:
            paid[person] -= ate[person]
            if paid[person] == 0:
                del paid[person]
            del ate[person]
    days = 0
    needTobuy = 0
    while True:
        days += 1
        ateToday = set()
        for person in ate:
            if ate[person] > 0:
                for dinner in paid:
                    if paid[dinner] > 0:
                        if dinner in ateToday:
                            continue
                        ateToday.add(dinner)
                        ate[person] -= 1
                        paid[dinner] -= 1
                        needTobuy += 1
        if max(paid.values()) == 0:
            break
    output.append((needTobuy, days))

for o in output:
    print(f"{o[0]} {o[1]}")
