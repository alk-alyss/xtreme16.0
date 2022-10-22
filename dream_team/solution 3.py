def counter(l, limits):
    # index = 0
    changed = False
    for index in range(5):
        if l[4 - index] + 1 >= limits[4 - index] and index < 4:
            l[4 - index - 1] += 1
            l[4 - index] = 0
            changed = True
        if index == 4:
            if l[0] + 1 >= limits[0]:
                return limits
    if not changed:
        l[4] += 1
    return l


def main():
    B = int(input())
    P = int(input())
    point_guards = [input().split(" ") for _ in range(P)]
    point_guards = [[i[0], int(i[1])] for i in point_guards]
    G = int(input())
    shooting_guards = [input().split(" ") for _ in range(G)]
    shooting_guards = [[i[0], int(i[1])] for i in shooting_guards]

    S = int(input())
    small_forward = [input().split(" ") for _ in range(S)]
    small_forward = [[i[0], int(i[1])] for i in small_forward]

    F = int(input())
    power_forward = [input().split(" ") for _ in range(F)]
    power_forward = [[i[0], int(i[1])] for i in power_forward]

    C = int(input())

    centers = [input().split(" ") for _ in range(C)]
    centers = [[i[0], int(i[1])] for i in centers]
    players = [point_guards, shooting_guards, small_forward, power_forward, centers]

    for player in players:
        player.sort(key=lambda x: x[0], reverse=False)
        player.sort(key=lambda x: x[1], reverse=True)

    # selected = ['' for i in range(5)]
    budg = 0
    # p, g, s, f, c = 0, 0, 0, 0, 0
    ls = [0, 0, 0, 0, 0]
    limits = [P, G, S, F, C]
    mx = 0
    mxls = []
    while ls != limits:
        print(ls, limits)
        # print([ls[i] for i in range(5)])
        # print([len(i) for i in players])
        selected = [players[i][ls[i]] for i in range(5)]

        print(selected)
        # print(selected)
        summ = sum([x[1] for x in selected])
        print(summ)
        if summ <= B:
            print('in', summ)

            if mx >= summ:
                mx = summ
                mxls = [i for i in selected]
                print(mxls)
                # return print('\n'.join([x[0] for x in selected]))
        ls = counter(ls, limits)
    print(mxls)
    print('\n'.join([x[0] for x in mxls]))


if __name__ == '__main__':
    main()
    # ls = [0, 0, 0, 0, 0]
