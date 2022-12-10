Angle = [0.698132, 0.959931, 1.134464, 1.570796, 1.919862]
Torque = [0.188224, 0.209138, 0.230052, 0.250965, 0.313707]

# y = a0 + a1x
sumXi = sum(Angle)
sumZi = sum(Torque)
sumXiZi = 0
sumXiSquare = 0
n = len(Angle)
for i in range(0, len(Angle)):
    sumXiZi = sumXiZi + Angle[i] * Torque[i]
    sumXiSquare = sumXiSquare + Angle[i]**2

a1 = ((n*sumXiZi) - (sumXi*sumZi))/ ((n*sumXiSquare) - (sumXi**2))
meanX = sumXi / n
meanZ = sumZi / n

a0 = meanZ - meanX*a1

x = float(input("Enter an angle : "))
y = a0 + a1*x
print("The Predicted value after Linear Regression :",y)