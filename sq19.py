s='quick brown fox jumps right over the lazy dog'

len(set(filter(str.isalpha,s)))==26

len({x for x in s if x.isalpha()})==26

l=[False]*26
for c in s.lower():
 if c.isalpha(): l[ord(c)-97]=1
all(l)


