def interest(principal):
  if principal < 0 :
    print("Invalid Principal.")
    return -1
  elif principal >=0 and principal < 1000:
    profit = 0
    return profit
  elif principal >=1000 and principal <10000 :
    profit = 0.1 * principal
    return profit
  elif principal >= 10000 and principal < 50000:
    profit = 0.05 * principal
    return profit
  else :
    profit = 0.025 * principal
    return profit

def profit_prin(principal):
  profit = interest(principal)
  total = profit + principal
  return total

princ = float(input("Enter your total Principal : "))

total = profit_prin(princ)
print("Profit-Principal is :",total)