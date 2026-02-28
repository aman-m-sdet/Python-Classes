#WAP to find non occurance of each vowel present in given string?

s = input("enter some string to search vowel: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
d = {}
for ch in s:
    if ch in vowels:
        d[ch] = d.get(ch, 0) + 1
for k, v in sorted(d.items()):
    print("{} occurs {} times".format(k, v))


# enter some string to search vowel:     Aman Software solutions
# a occurs 3 times
# e occurs 1 times
# i occurs 1 times
# o occurs 3 times
# u occurs 1 times