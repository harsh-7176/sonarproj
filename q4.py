l=input("\nEnter Characters and Strings separated by space : ")
print()
print(''.join(set(l)))

d=''
for c in l:
 if c not in d:
   d=d+c
print(d)

print(''.join({c for c in l}))