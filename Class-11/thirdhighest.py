information = {

    "student" : ['Bruce', 'Clark', 'Hal', 'Diana', 'Barry'],
    "id" : [1212, 1214, 1414, 1322, 1955],
    "marks" : [89, 78, 11, 77, 90]
}


for i in range(0, len(information["marks"])):
    for j in range(0, len(information["marks"])-1):
        if information["marks"][j] > information["marks"][j+1]:
            swap1 = information["marks"][j]
            swap2 = information["student"][j]
            information["marks"][j] = information["marks"][j+1]
            information["student"][j] = information["student"][j+1]
            information["marks"][j + 1] = swap1
            information["student"][j+1] = swap2


print("The third highest is " + str(information["student"][-3]) + " with " + str(information["marks"][-3]))

