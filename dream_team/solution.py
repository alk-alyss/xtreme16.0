def main():
    B = int(input())
    P = int(input())
    point_guards = [input().split(" ") for _ in range(P)]
    G = int(input())
    shooting_guards = [input().split(" ") for _ in range(G)]
    S = int(input())
    small_forward = [input().split(" ") for _ in range(S)]
    F = int(input())
    power_forward = [input().split(" ") for _ in range(F)]
    C = int(input())
    centers = [input().split(" ") for _ in range(C)]
    players = [centers, power_forward, small_forward, shooting_guards, point_guards]
    for player in players:
        player.sort(key=lambda x: (x[1], x[0]), reverse=True)
    # C, F, S, G, P = 0, 0, 0, 0, 0
    team = [(players[i][0][1], players[i][0][0]) for i in range(5)]

    selected = []
    for p in range(P):
        for g in range(G):
            for s in range(S):
                for f in range(F):
                    for c in range(C):
                        pass


if __name__ == '__main__':
    main()
