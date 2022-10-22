def normalizeDegree(degree):
    while degree < 0:
        degree += 360

    degree %= 360

    if degree >= 180:
        degree -=  180

    return degree


T = int(input())

output = ""

for _ in range(T):
    x = input().split()

    N = int(x[0])

    if N == 0:
        output += str(1) + '\n'
        continue

    degrees = list(map(int, x[1:]))

    s = set()
    for degree in degrees:
        s.add(normalizeDegree(degree))

    output += str(len(s)*2) + '\n'

print(output)
