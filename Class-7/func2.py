TwoDList = [
    [5,7,9,10],
    [5,6,5],
    [50,2,3],
    [9,8,7,6,3,4,8,9],
    [40,10]
]

def highestList(nums):
    idx = 0
    max = -1
    for i in range(0, len(nums)):
        ans = sum(nums[i])
        if ans > max :
            max = ans
            idx = i
    final = nums[idx]
    return final


ans = highestList(TwoDList)
print(ans)