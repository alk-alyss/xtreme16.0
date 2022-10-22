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

    # for player in players:
    #     player.sort(key=lambda x: x[0], reverse=False)
    #     player.sort(key=lambda x: x[1], reverse=True)
    mx = 0
    mxls = []
    for p in range(P):
        for g in range(G):
            for s in range(S):
                for f in range(F):
                    for c in range(C):
                        selected = [players[i][v] for i, v in enumerate([p, g, s, f, c])]

                        print(selected)

                        summ = sum([x[1] for x in selected])
                        # summ = sum(selected)

                        if summ <= B:
                            if summ >= mx:
                                mx = summ
                                mxls = selected.copy()

    print('\n'.join([x[0] for x in mxls]))


if __name__ == '__main__':
    main()
