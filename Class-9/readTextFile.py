file = open("Message.txt", "r")

cnt = 6

print(cnt)

person1 = []
person2 = []
message = []
for i in range(0, cnt):
        message.append(file.readline())

for i in range(0, len(message)):
    if (i+1)%2 != 0:
        person1.append(message[i][0:len(message[i])-1])
    else:
        person2.append(message[i][0:len(message[i])-1])

print(person1)
print(person2)