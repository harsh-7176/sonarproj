s=input('\nEnter a String : ')
print()
p=s[::-1]
print(p)
print()
p=''.join(reversed(s))
print(p)
print()
r=''
for c in s:
 r=c+r
print(r)
