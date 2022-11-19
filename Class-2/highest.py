#Dictionary
studs = {
  'Max' : [87, 88, 56],
  'Ron' : [56,88,90],
  'Potter' : [82,80,86],
  'Harry' : [78,96,99],
}
highest = ''
for i in studs: 
  sum1 = sum(studs[i])
  studs[i].append(sum1/len(studs[i]))

maximum = -1
for i in studs:
  if maximum < studs[i][len(studs[i])-1]:
    maximum = studs[i][len(studs[i])-1]
    highest = i
print(highest,maximum)
