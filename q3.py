l=input("\nEnter Characters and Strings separated by space : ")
print()
print(list(l))

x=[]
for c in l:
 x.append(c)

print(x)

x=[]
x=[c for c in l]

print(x)