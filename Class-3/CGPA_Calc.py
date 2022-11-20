dict = {
  "name" : "Ahsan",
  "subjects" : ["CSE","Math","EEE","Eng"],
  "credit" : [3,3.5,4,2],
  "marks" : [],
  "grade" : []
}
#We will take user input of marks
i = 0
while(i!=len(dict["subjects"])):
  marks = float(input("Enter Marks of "+dict["subjects"][i]+" : "))
  dict["marks"].append(marks)
  i = i + 1

for marks in dict["marks"]:
  grade = 0
  if marks>=80 :
    grade = 4
  elif marks >=70 and marks <80:
    grade = 3
  elif marks >=60 and marks <70:
    grade = 2
  else : 
    grade = 0
  dict["grade"].append(grade)
print(dict["grade"])

sumCredits = sum(dict["credit"])

sum = 0
for i in range(0, len(dict["credit"])):
  sum = sum + dict["credit"][i]*dict["grade"][i]
  if dict["grade"][i]==0:
    sum = 0
    break
cgpa = sum/sumCredits

print(cgpa)

  
