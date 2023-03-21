x='listen'
y='silent'

from collections import Counter
Counter(x)==Counter(y)#Counter makes dictionary

sorted(x)==sorted(y)

for c in set(x):
 if x.count(c)!=y.count(c):
  print('\nStrings are not Anagrams..')
  break
else:
 print('\nThe Strings are Anagrams..')
