from functools import cache

@cache
def is_valid_string(string):
    if len(string) == 1:
        return True

    # if len(string) % 2 == 0 and string[:len(string) // 2] == string[len(string) // 2:]:
    #     return True

    for s in string:
        if s < string[0]: return False

    for i in range(1, len(string)):
        s1 = string[:i]
        s2 = string[i:]

        if s1 > s2: continue

        if not is_valid_string(s1): continue
        if not is_valid_string(s2): continue

        if s1 <= s2: return True


N = int(input())

output = ""

for _ in range(N):
    s = input()
    output += '1' if is_valid_string(s) else '0'

print(output)
