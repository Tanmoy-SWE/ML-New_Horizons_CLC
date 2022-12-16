information = {

    "student" : ['Bruce', 'Clark', 'Hal', 'Diana', 'Barry'],
    "id" : [1212, 1214, 1414, 1322, 1955],
    "marks" : [99, 77, 55, 68, 90]
}

max = -1
idx = 0

for i in range(0, len(information["marks"])):
    if information["marks"][i] > max:
        max = information["marks"][i]
        idx = i
print(information["student"][i])


