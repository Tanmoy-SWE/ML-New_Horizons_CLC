#Element add at last
val = [7,4,6,9,8,2,5,10,6,8,25,35]
val.append(5)
print(val)


def onlyEven(nums, n):
    temp = []
    for i in nums:
        if i % n == 0:
            temp.append(i)
        elif i%2 == 0 :
            temp.append(i)
        elif i%2 != 0:
            pass
    return temp
print(onlyEven(val,5))