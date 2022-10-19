def is_valid_string(s):
    if len(s) == 1:
        return True

    for i in range(1, len(s)):
        s1 = s[:i]
        s2 = s[i:]

        if s1 > s2 : continue

        if not is_valid_string(s1): continue
        if not is_valid_string(s2): continue

        if s1 <= s2: return True



N = int(input())

output = ""

for _ in range(N):
    s = input()
    output += '1' if is_valid_string(s) else '0'

print(output)
