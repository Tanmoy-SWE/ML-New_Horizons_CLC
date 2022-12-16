file = open("numbers.txt", "r")

numbers = []
n = 5
numbers_float = []
for i in range(0,n):
    p = file.readline()
    numbers.append(p[0:len(p)-1])

for j in range(0, len(numbers)):
    numbers_float.append(float(numbers[j]))

sum41 = sum(numbers_float)
avg = sum41/len(numbers_float)
print(avg)