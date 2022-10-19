from functools import cache

# @cache
# def is_valid_string(string):
#     if len(string) == 1:
#         return True

#     # if len(string) % 2 == 0 and string[:len(string) // 2] == string[len(string) // 2:]:
#     #     return True

#     for s in string:
#         if s < string[0]: return False

#     for i in range(1, len(string)):
#         s1 = string[:i]
#         s2 = string[i:]

#         if s1 > s2: continue

#         if not is_valid_string(s1): continue
#         if not is_valid_string(s2): continue

#         if s1 <= s2: return True

def is_valid_string(string):
    # substrings = []
    # index = 0
    # while index < len(string):
    #     substring = string[index]
    #     for i,s in enumerate(string[index+1:]):
    #         if substring <= s:
    #             substring += s
    #         else:
    #             substrings.append(substring)
    #             index += i
    #             break

    # next_substrings = []
    # index = 0
    # while index < len(substrings):
    #     substring = substrings[index]
    #     for i,s in enumerate(substrings[index+1:]):
    #         if substring <= s:
    #             substring += s
    #         else:
    #             next_substrings.append(substring)
    #             index += 1
    #             break

    substrings = list(string)
    new_substrings = []
    prevLen = len(substrings)
    index = 0
    while True:
        s1 = substrings[index]
        if index >= len(substrings):
            if prevLen == len(substrings):
                break

            substrings = new_substrings
            prevLen = len(substrings)
            index = 0
            continue

        s2 = substrings[index+1]

        if s1 <= s2:
            s1 += s2
            new_substrings.extend(substrings[:index])
            new_substrings.append(s1)
            # TODO what if index+2 does not exist
            new_substrings.extend(substrings[index+2:])
            index = 0
        else:
            index += 1

    # print(substrings)

    if len(substrings) == 1:
        return True

    return False


N = int(input())

output = ""

for _ in range(N):
    s = input()
    output += '1' if is_valid_string(s) else '0'

print(output)
