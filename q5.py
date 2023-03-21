l=input("\nEnter Characters and Strings separated by space : ")
print()
cnt=0
for c in l:
 if c in 'aeiou':
  cnt=cnt+1
print(cnt)