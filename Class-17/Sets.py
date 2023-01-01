coins = ['H', 'T']
dice = ['1', '2', '3', '4', '5', '6']
Dice_Coins = []

for i in range(0, len(coins)):
    for j in range(0, len(coins)):
        for k in range(0, len(dice)):
            Dice_Coins.append(coins[i]+coins[j]+dice[k])
print(Dice_Coins)
cnt = 0
for i in Dice_Coins:
    if i == 'TT3':
        cnt = cnt +1
prob = cnt / len(Dice_Coins)

print("The probability of having TTH is :", prob)