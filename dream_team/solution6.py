def main():
    B = int(input())
    P = int(input())
    # pg = input().split(" ")
    # point_guards = [input().split(" ") for _ in range(P)]
    f = lambda x: (x[0], int(x[1]))
    point_guards = [f(input().split(" ")) for _ in range(P)]
    # print(point_guards)
    # point_guards = [[i[0], int(i[1])] for i in point_guards]
    G = int(input())
    # shooting_guards = [input().split(" ") for _ in range(G)]
    shooting_guards = [f(input().split(" ")) for _ in range(G)]
    # shooting_guards = [[i[0], int(i[1])] for i in shooting_guards]

    S = int(input())
    # small_forward = [input().split(" ") for _ in range(S)]
    small_forward = [f(input().split(" ")) for _ in range(S)]
    # small_forward = [[i[0], int(i[1])] for i in small_forward]

    F = int(input())
    # power_forward = [input().split(" ") for _ in range(F)]
    power_forward = [f(input().split(" ")) for _ in range(F)]
    # power_forward = [[i[0], int(i[1])] for i in power_forward]

    C = int(input())

    centers = [f(input().split(" ")) for _ in range(C)]
    # centers = [input().split(" ") for _ in range(C)]
    # centers = [[i[0], int(i[1])] for i in centers]
    players = [point_guards, shooting_guards, small_forward, power_forward, centers]
    print(players)
    # mx = 0
    # mxls = [[]]
    # for p in range(P):
    #     for
    # g in range(G):
    # for s in range(S):
    #     for
    # f in range(F):
    # for c in range(C):
    #     selected = [players[i][v] for i, v in enumerate([p, g, s, f, c])]
    # summ = sum([x[1] for x in selected])
    # if summ < B:
    #     if
    # summ > mx:
    # mx = summ
    # mxls[0] = [i for i in selected]
    #
    # elif summ == mx:
    # mxls.append([i for i in selected])

    #
    #                     # print(selected)
    #
    #                     summ = sum([x[1] for x in selected])
    #
    #                     if summ <= B:
    #                         if summ > mx:
    #                             mx = summ
    #                             # if len(mxls) == 1:
    #                             mxls[0] = selected.copy()
    #                         elif summ == mx:
    #                             mxls.append(selected.copy())
    # if len(mxls) > 1:
    #     # final = sorted([''.join(x[0] for x in mxls[i]) for i in range(len(mxls))])[0]
    #     final = sorted([mxls[i] for i in range(len(mxls))])[0]
    #     print('\n'.join([x[0] for x in final]))
    #
    # else:
    #     print('\n'.join([x[0] for x in mxls[0]]))


if __name__ == '__main__':
    main()
