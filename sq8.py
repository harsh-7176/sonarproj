import math
s=input('\nEnter a String : ')
print()
n=int(math.ceil(len(s)**.5))
for i in range(n):
 print(s[i*n : (i+1)*n].ljust(n,'*'))
print()
print('\n'.join([s[i*n:(i+1)*n].ljust(n,'*')for i in range(n)]))