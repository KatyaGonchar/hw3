def reverse_part(s, n):
    part = s[:n]
    return part + part[:-1][::-1]


s = "abcdefghijklmnopqrstuvwxyz"
assert(reverse_part(s, 1)) == "a"
assert(reverse_part(s, 2)) == "aba"
assert(reverse_part(s, 3)) == "abcba"
assert(reverse_part(s, 4)) == "abcdcba"
