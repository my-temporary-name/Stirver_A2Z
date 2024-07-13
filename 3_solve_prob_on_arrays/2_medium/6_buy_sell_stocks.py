prices = [7,1,5,3,6,4]

mx = 0
min_price = float('inf')

for i in range(len(prices)):
    min_price = min(min_price , prices[i])
    mx = max(mx , prices[i] - min_price)

print(mx)