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

t = [0,10,15,20,22.5,30]

min_max_v_t = []
min_max_t = []
for k in range(0, len(temp)):
    if temp[k] == -1:
        min_max_t.append(t[k])
        min_max_v_t.append(v_t[k])

print(min_max_t)
print(min_max_v_t)

diff_of_t = min_max_t[1] - min_max_t[0]
diff_of_v_t = min_max_v_t[1] - min_max_v_t[0]

gradient = diff_of_v_t / diff_of_t
print(gradient)
diff = target - min_max_t[0]
print(diff)
addition = gradient * diff
print(addition)

final_v_t = min_max_v_t[0] + addition
print(final_v_t)