import math
list = [5,4,9,2,5,12,43,4,9,6,12,22,43,15]
unique = []
for i in list:
  if i not in unique:
    unique.append(i)
print(unique)
