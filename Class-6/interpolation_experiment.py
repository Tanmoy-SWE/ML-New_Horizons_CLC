house = {
  'area' : [1250,1300,1500,1600,2000,2200],
  'rent' : [25000, 30000, 35000, 38000, 45000, 50000]
}

wish = int(input("Enter the size of the house :"))

print(house['area'])
Maxidx = 0
for i in range(0,len(house['area'])):
  diff = wish - house['area'][i]
  if diff <= 0 :
    Maxidx = i
    break
Minidx = Maxidx - 1

diff_of_area = house["area"][Maxidx] - house["area"][Minidx]
diff_of_rent = house["rent"][Maxidx] - house["rent"][Minidx]

rate = diff_of_rent / diff_of_area

diff = wish - house["area"][Minidx]

addition = rate * diff

final_rent = house["rent"][Minidx]+addition
print(final_rent)

diff2 = house["area"][Maxidx] - wish
subtraction = rate * diff2

final_rent2 = house["rent"][Maxidx] - subtraction
print(final_rent2)
