from collections import defaultdict


def default():
    return 0


T = int(input())

output = []
for _ in range(T):
    paid = defaultdict(default)
    ate = defaultdict(default)
    M = int(input())
    for _ in range(M):
        meal = input().split()
        paid[meal[0]] += int(meal[1])
        for person in range(2, len(meal)):
            ate[meal[person]] += 1
    for person in ate:
        if person in paid:
            if paid[person] >= ate[person]:
                paid[person] -= ate[person]
                ate[person] = 0
            else:
                ate[person] -= paid[person]
                paid[person] = 0
    toBuy = sum(ate.values())
    days = max(paid.values())
    output.append((toBuy, days))
for o in output:
    print(f"{o[0]} {o[1]}")
