players = {
  "name" : ["messi","ronaldo","neymar"],
  "height" : [168.4, 182, 170],
  "weight" : [68, 82, 62],
  'bmi' : []
}
#convert heights in cm -> m
for i in range(0, len(players["height"])):
  players["height"][i] = players["height"][i]/100

for i in range(0, len(players["height"])):
  players["bmi"].append(players["weight"][i]/(players["height"][i]**2))
#print(players)

max = -1
idx = 0
for i in range(0, len(players["bmi"])):
  if max < players["bmi"][i]:
    max = players["bmi"][i]
    idx = i
print("the player wth max bmi:" + players["name"][idx])  
