s=input('\nEnter a String : ')
print()
r=''.join(set(s))
print(r)
print()
d=''
for c in s:
 if c not in d: d=d+c
print(d)