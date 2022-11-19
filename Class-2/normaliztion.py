list = [5, 4, 9, 2, 6, 12, 22, 43, 15]
max = -1
min = 99999
norm_list = []
for i in range(0, len(list)):
  
  if min > list[i]:
    min = list[i]
print(min)

for i in range(0, len(list)):
  
  if max < list[i]:
    max = list[i]
print(max)

for i in range(0, len(list)):
  x_norm = (list[i]-min)/(max-min)
  list[i] = x_norm
print(list)
