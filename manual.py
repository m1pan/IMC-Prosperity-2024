best_bounds = [0,0]
best_profit = 0
for i in range(0,100):
    for j in range(i+1,100):        
        profit = (100-i)*((i/100)**2) + (100 - j)*((j/100)**2 - (i/100)**2)
        if profit > best_profit:
            best_profit = profit
            best_bounds = [i,j]

print(best_bounds)
print(best_profit)