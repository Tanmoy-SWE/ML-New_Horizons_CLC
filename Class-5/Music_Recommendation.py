import random
#Creating a uniform spectrum
weights = {
   1 : 'Jazz',
   2 : 'Pop',
   3 : 'Country',
   4 : 'Rap',
   5 : 'Rock',
   6 : 'Metal'
}

data = [5,4,5,1,5,6,5,5,5,5,5,5,6,6,6,6,6,6,2,2,3,2,4]

mean = sum(data)/len(data)

diff_from_mean = []
for i in weights:
  diff_from_mean.append(abs(i-mean))

least = 99999
idx = 0
for i in range(0,len(diff_from_mean)):
  if least > diff_from_mean[i]:
    least = diff_from_mean[i]
    idx = i

songsDict = {
  1 : ['Beyond Horizon','abc'],
  2 : ['Beat It','Wavin Flag'],
  3 : ['Country Roads','Annies Song'],
  4 : ['Not Afraid','MockingBird'],
  5 : ['Nothing else Matters','Smells Like a teen spirit','Heart Shaped Box', 'Lonely Day','Do I wanna know', 'Angels fall', 'I wanna be yours'],
  6 : ['Psychosocial','Chop Suey']
}

songWeight = idx + 1
print(songsDict[songWeight])
n = random.randint(0,len(songsDict[songWeight])-1)
print(songsDict[songWeight][n])
