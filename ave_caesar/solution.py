def is_valid_string(string):
    splits = list(range(len(string)))

    start = 0
    end = 0
    prevLen = len(splits)
    while True:
        if len(splits) == 1:
            return True

        if len(splits) == prevLen:
            return False

        s1 = string[splits[end]:splits[end+1]]
        end += 1
        s2 = string[splits[end]:splits[end+1]]

        if s1 == [] or s2 == []:
            start = 0
            end = start

        if s1<=s2:
            splits.pop(end)
        else:
            start += 1
            end = start


N = int(input())

output = ""

for _ in range(N):
    s = input()
    output += '1' if is_valid_string(s) else '0'

print(output)
