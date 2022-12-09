from csv_reader import sepal_length

print(sepal_length)

del sepal_length[0]

print(sepal_length)

sepal_length_new = []

for i in range(0,len(sepal_length)):
    sepal_length_new.append(float(sepal_length[i]))

print(sepal_length_new)

cnt = 0
firstSum = 0
for i in range(len(sepal_length_new)):
    if sepal_length_new[i] < 10 :
        cnt = cnt + 1
        firstSum = firstSum + sepal_length_new[i]

avg = firstSum / cnt

for i in range(len(sepal_length_new)):
    if sepal_length_new[i] >= 10:
        sepal_length_new[i] = avg

sumLength = sum(sepal_length_new)
mean = sumLength / len(sepal_length_new)
print("The mean of sepal_length :",mean)