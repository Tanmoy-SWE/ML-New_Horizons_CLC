def cntPos(num):
    pos = []
    for i in num:
        if i >=0 :
           pos.append(i)
    return pos

list = [-6,9,10,-8,6,-3]
ans = cntPos(list)
print(ans)