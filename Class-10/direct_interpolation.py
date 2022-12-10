t = [0,10,15,20,22.5,30]
v_t = [0,227.04,362.78,517.35,602.97,901.67]

#first order polynomial
# v(16) = ?

diff = []
target = 16

for i in range(0, len(t)):
    sub = abs(t[i]-target)
    diff.append(sub)
print(diff)

temp = t

order = 2
for j in range(0, order):
    small = 9999
    idx = 0
    for i in range(0, len(diff)):
        if diff[i] < small:
            small = diff[i]
            idx = i
    diff[idx] = 10000
    temp[idx] = -1
print(temp)
