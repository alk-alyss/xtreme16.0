def lf(x):
    return [x[0], int(x[1])]


def main():
    B = int(input())

    P = int(input())
    point_guards = [lf(input().split(" ")) for _ in range(P)]
    G = int(input())

    shooting_guards = [lf(input().split(" ")) for _ in range(G)]

    S = int(input())
    small_forward = [lf(input().split(" ")) for _ in range(S)]

    F = int(input())
    power_forward = [lf(input().split(" ")) for _ in range(F)]

    C = int(input())
    centers = [lf(input().split(" ")) for _ in range(C)]

    players = [point_guards, shooting_guards, small_forward, power_forward, centers]
    dt = []
    maxsum = 0
    maxls = [[]]
    for p in range(P):
        for g in range(G):
            for s in range(S):
                for f in range(F):
                    for c in range(C):
                        t = [point_guards[p], shooting_guards[g], small_forward[s], power_forward[f], centers[c]]
                        summing = sum([x[1] for x in t])
                        # print(summing)
                        if summing <= B:

                            if summing > maxsum:
                                maxsum = summing
                                # maxls = t.copy()
                                maxls[0] = t.copy()
                            elif summing == maxsum:
                                if len(maxls) == 1:
                                    maxls.append(t)
    # print(maxls)
    if len(maxls) > 1:
        # print(maxls[0], '\n', maxls[1])
        print('\n'.join([x[0] for x in sorted(maxls)[0]]))
    else:
        print('\n'.join([x[0] for x in maxls[0]]))


if __name__ == '__main__':
    main()
#     50/100 score
test_case = """235000
3
curry 40000
nash 20000
johnson 10000
3
jordan 50000
wade 20000
bryant 80000
1
james 30000
1
duncan 60000
1
oneal 100000"""

test_case1="""235000
3
curry 40000
nash 20000
aohnson 20000
3
jordan 50000
wade 20000
bryant 80000
1
james 30000
1
duncan 60000
1
oneal 100000"""

test_case2="""
235000
3
curry 40000
nash 20000
johnson 20000
4
jordan 50000
wade 20000
owen 20000
bryant 80000
1
james 30000
1
duncan 60000
1
oneal 100000"""