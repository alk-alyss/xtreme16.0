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
    first_string = string[0]
    index = 1
    for i,s in enumerate(string[index:]):
        if first_string <= s:
            first_string += s
        else:
            index += i
            break

    second_string = string[index]
    for s in string[index+1:]:
        if second_string <= s:
            second_string += s

        else:
            return False

    return first_string <= second_string


N = int(input())

output = ""

for _ in range(N):
    s = input()
    output += '1' if is_valid_string(s) else '0'

print(output)
