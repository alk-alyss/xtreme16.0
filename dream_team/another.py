def find_smallest_diff(players, indexes):
    diff = -1
    index_changed = -1
    for i, player in enumerate(players):
        if indexes[i] + 1 == len(player):
            continue
        indexes[i] += 1
        if diff == -1:
            diff = player[indexes[i]][1]
            index_changed = i
        elif diff < player[indexes[i]][1]:
            diff = player[indexes[i]][1]
            indexes[index_changed] -= 1
            index_changed = i
        elif diff == player[indexes[i]][1]:
            if player[indexes[i]][0] < player[index_changed][0]:
                indexes[index_changed] -= 1
                index_changed = i
        else:
            indexes[i] -= 1
    return indexes, diff


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
    players = [point_guards, shooting_guards,
               small_forward, power_forward, centers]
    max_budget = 0
    for player in players:
        player.sort(key=lambda x: (x[1], x[0]), reverse=True)
    for player in players:
        max_budget += player[0][1]
    for player in players:
        for i in range(len(player)-1, 0, -1):
            player[i][1] = player[i-1][1] - player[i][1]
        player[0][1] = 0
        # print(player)

    C, F, S, G, P = 0, 0, 0, 0, 0
    indexes = [C, F, S, G, P]
    # print(max_budget)
    while max_budget > B:
        indexes, diff = find_smallest_diff(players, indexes)
        max_budget -= diff
        # print(indexes, max_budget)
    for i in range(5):
        print(players[i][indexes[i]][0])


if __name__ == '__main__':
    main()
