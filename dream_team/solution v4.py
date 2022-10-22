def counter(ls, limits):
    ls[0] += 1
    for i in range(4):
        if ls[i] == limits[i]:
            ls[i] = 0
            if ls[i + 1] + 1 < limits[i + 1]:
                ls[i + 1] += 1
    if ls[4] >= limits[4]:
        return ls


# def counter(ls, limits):
#     ls[4] += 1
#     for i in range(1, 5):
#         if ls[4 - i + 1] == limits[4 - i + 1]:
#             ls[4 - i + 1] = 0
#             if ls[4 - i] + 1 < limits[4 - i]:
#                 ls[4 - i] += 1
#     if ls[0] >= limits[0]:
#         return ls


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

    ls = [0, 0, 0, 0, 0]
    limits = [P, G, S, F, C]
    while ls != limits:
        print(ls)
        selected = [players[i][ls[i]] for i in range(5)]

        summ = sum([x[1] for x in selected])
        if summ <= B:
            print('\n'.join([x[0] for x in selected]))
        counter(ls, limits)
        if ls == [i - 1 for i in limits]:
            break


if __name__ == '__main__':
    main()
