def buy_and_sell_stock_once(prices):
    tmax=0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            val=prices[j]-prices[i]
            tmax=max(tmax,val)
    return tmax

prices=[310,315,275,295,260,270,290,230,255,250]
print(buy_and_sell_stock_once(prices))