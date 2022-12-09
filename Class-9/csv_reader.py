import csv

sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
species = []
with open('iris.csv') as fileIris:

    #Reading the whole csv file
    readed_data = csv.reader(fileIris)

    for row in readed_data:
        sepal_length.append(row[0])
        sepal_width.append(row[1])
        petal_length.append(row[2])
        petal_width.append(row[3])
        species.append(row[4])
