arr = [4,-6,7,2,8,-5]
arr.sort()
print(arr)
max = len(arr)-1
min = 0
num = 70
while(True):
  mid = (max + min)//2
  if arr[mid]>num:
    min = min
    max = mid-1
  elif arr[mid] < num:
    max = max
    min = mid+1
  else:
    print("The number is found")
    break
  if min >= max:
    print("The number is not found")
    break
