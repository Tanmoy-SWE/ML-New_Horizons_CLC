from itertools import combinations
nums = [5,2,-4,-3,6,-5,2]
combs = combinations(nums,3)
combs = list(combs)
print(combs)
max = -9999999
for i in range(0, len(combs)):
    sum = 0
    for j in combs[i]:
        sum = sum + j
    if sum > max:
        max = sum
print("The maximum sum is : ",max)
