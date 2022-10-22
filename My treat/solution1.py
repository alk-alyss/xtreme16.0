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


def main():
    T = get_number()
    d = [{get_word(): [get_word() for _ in range(get_number())] for _ in range(get_number())} for _ in
         range(T)]
    print(d)


if __name__ == '__main__':
    main()
