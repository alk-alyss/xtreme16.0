# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def dancer(command, man, default=True):
    default_man = [[' ', 'o', ' '], ['/', '|', '\\'], ['/', ' ', '\\']]
    # man = [[' ', 'o', ' '], ['/', '|', '\\'], ['/', ' ', '\\']]
    d = {"right": 0, "left": 2, "head": 0, 'hip': 1, 'leg': 2}

    command = command.split()
    if 'say' in command:
        print(' '.join(command[1:]))
    else:
        if command[1]=='head':
            man[d["head"]][d[command[0]]] = '(' if command[0] == 'right' else ')'
            man[d["hip"]][d[command[0]]] = ' '
        if command[1] == 'hand' and command[3] == 'hip':
            man[d["hip"]][d[command[0]]] = '<' if command[0] == 'right' else '>'
            man[d["head"]][d[command[0]]] = ' '
        if command[1] == 'hand' and command[3] == 'start':
            man[d["hip"]][d[command[0]]] = '/' if command[0] == 'right' else '\\'
            man[d["head"]][d[command[0]]] = ' '

        if command[1] == 'leg':
            if command[2] == 'in':
                man[d["leg"]][d[command[0]]] = '<' if command[0] == 'right' else '>'
            if command[2] == 'out':
                man[d["leg"]][d[command[0]]] = '/' if command[0] == 'right' else '\\'

            # man[d["leg"]][d[command[0]]]=' '
        if command[0] == 'turn':
            for i in range(3):
                man[i] = man[i][::-1]
            # print('-', ''.join(man[2]))
            # print('=', ''.join(man[2][::-1]))

            if man[0][0] == ')':
                man[0][0] = '('
            if man[0][2] == '(':
                man[0][2] = ')'

            if man[1][0] == '>':
                man[1][0] = '<'
            if man[1][2] == '<':
                man[1][2] = '>'

            if man[1][0] == '\\':
                man[1][0] = '/'
            if man[1][2] == '/':
                man[1][2] = '\\'

            if man[2][0] == '>':
                man[2][0] = '<'
            if man[2][2] == '<':
                man[2][2] = '>'

            if man[2][0] == '\\':
                man[2][0] = '/'
            if man[2][2] == '/':
                man[2][2] = '\\'
        for i in man:
            print(''.join(i))


def main():
    T = int(input())
    for _ in range(T):
        man = [[' ', 'o', ' '], ['/', '|', '\\'], ['/', ' ', '\\']]
        n = int(input())
        for _ in range(n):
            dancer(input(), man)


if __name__ == '__main__':
    main()
