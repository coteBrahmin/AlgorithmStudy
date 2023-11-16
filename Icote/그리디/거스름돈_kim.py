import sys
N = int(sys.stdin.readline())
temp = N
coins = {500:0, 100:0, 50:0, 10:0}
for coin in coins:
  coins[coin] = temp//coin
  temp %= coin
print(sum(coins.values()))