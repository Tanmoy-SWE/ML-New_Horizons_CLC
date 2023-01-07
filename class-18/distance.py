items = {
    "fish" : ['salmon', 'salmon', 'eel', 'hilsha', 'salmon', 'hilsha', 'eel', 'eel'],
    "coordinates" : [[3,4],[4,3],[5,5],[6,2],[2,1],[3,7],[5,7],[6,7]],
    "distance" : []
}


#Calculate and put the values of distance array in the items dictionary
x = int(input("Enter an x coordinate: "))
y = int(input("Enter a y coordinate: "))
for i in range(0, len(items["coordinates"])):
    x_i = (x - items["coordinates"][i][0])**2
    y_i = (y - items["coordinates"][i][1])**2
    distance = (x_i + y_i)**0.5
    items["distance"].append(distance)


print(items["fish"])
print(items["distance"])

temp_fish = items["fish"]
distances = items["distance"]


for i in range(0, len(distances)):
    for j in range(0, len(distances)-1):
        if distances[j] > distances[j+1]:
            swap1 = distances[j]
            swap2 = temp_fish[j]
            distances[j] = distances[j+1]
            temp_fish[j] = temp_fish[j+1]
            distances[j + 1] = swap1
            temp_fish[j+1] = swap2

print(temp_fish)
print(distances)

k = int(input("Enter a k: "))
elements = []
for i in range(0, k):
    elements.append(temp_fish[i])

print(max(elements))