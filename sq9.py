x=input('\nEnter a String : ')
y=input('\nEnter a String : ')
print()
q=''.join(sorted(set(x)&set(y)))
print(q)
print()
q=''.join(filter(lambda c : c in y,set(x)))
print(q)
print()
s=''
for c in set(x):
 if c in y : s=s+c
print(s)
print()
s=''.join([c for c in set(x) if c in y])
print(s)
