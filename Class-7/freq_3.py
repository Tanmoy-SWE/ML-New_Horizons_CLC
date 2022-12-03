num = [4,5,6,6,9,4,6,4,5]

ans = []
for i in range(0, len(num)):
    cnt = 1
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            cnt = cnt + 1
        if cnt == 3:
            ans.append(num[i])
            break

print(ans)
