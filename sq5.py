s=input('\nEnter a String : ')
print()
n=len([c for c in s if c in 'aeiou'])
print(n)
print()
n=0
for c in s:
 if c in 'aeiou': n+=1
print(n)
print()
n=len(list(filter(lambda x : x in 'aeiou',s)))
print(n)
