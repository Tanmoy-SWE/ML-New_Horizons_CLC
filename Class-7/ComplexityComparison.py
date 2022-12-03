def LinearSearch(list, num):
    cnt = 0
    for i in range(0, len(list)):
        cnt = cnt +1
        if list[i]==num :
            print("The number is found")
            return cnt
    print("The number is not found")
    return cnt

def BinarySearch(arr, num):
    arr.sort()
    print(arr)
    max = len(arr) - 1
    min = 0
    cnt  = 0
    while (True):
        cnt = cnt + 1
        mid = (max + min) // 2
        if arr[mid] > num:
            min = min
            max = mid - 1
        elif arr[mid] < num:
            max = max
            min = mid + 1
        else:
            print("The number is found")
            return cnt
        if min >= max:
            print("The number is not found")
            return cnt

test = [8,30,23,5,12,4,6]
searchNum = 100


ans = LinearSearch(test, searchNum)
print("Iterations needed for Linear Search : ",ans)

ans = BinarySearch(test, searchNum)
print("Iterations needed for Binary Search : ",ans)