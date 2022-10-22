def counter(l,step):
    



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
    # print(centers)
    # players = [centers, power_forward, small_forward, shooting_guards, point_guards]
    players = [point_guards, shooting_guards, small_forward, power_forward, centers]

    for player in players:
        # player.sort(key=lambda x: (x[1], x[0]), reverse=True)

        # player.sort(key=lambda x: x[0], reverse=False)
        player.sort(key=lambda x: x[1], reverse=True)
    # print(players)

    # for player in players:
    #     if len([player[i][1] for i in range(len(player))]) > len({player[i][1] for i in range(len(player))}):
    #         print('Same Value')

    # print(players[1])
    # C, F, S, G, P = 0, 0, 0, 0, 0
    # team = [(players[i][0][1], players[i][0][0]) for i in range(5)]

    selected = ['' for i in range(5)]
    budg = 0
    p, g, s, f, c = 0, 0, 0, 0, 0
    while c < C:
        while f < F:
            while s < S:
                while g < G:
                    while p < P:
                        if players[0][p][1] + budg <= B:
                            selected[0] = players[0][p][0]
                            budg += players[0][p][1]
                            break
                        budg -= players[0][p][1]
                        p += 1

                    if players[1][g][1] + budg <= B:
                        selected[1] = players[1][g][0]
                        budg += players[1][g][1]
                        break
                    budg -= players[1][g][1]
                    g += 1

                if players[2][s][1] + budg <= B:
                    selected[2] = players[2][s][0]
                    budg += players[2][s][1]
                    break
                budg -= players[2][s][1]
                s += 1

            if players[3][f][1] + budg <= B:
                selected[3] = players[3][f][0]
                budg += players[3][f][1]
                break
            budg += players[3][f][1]
            f += 1

        if players[4][c][1] + budg <= B:
            selected[4] = players[4][c][0]
            budg += players[4][c][1]
            break
        budg -= players[4][c][1]
        c += 1

    print('\n'.join(selected))


if __name__ == '__main__':
    main()
