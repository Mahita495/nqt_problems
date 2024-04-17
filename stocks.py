stock_price = [8, 4, 12, 9, 20, 1]
#to find max profit only
n=len(stock_price)
i,j=0,1
profit=max_profit =0
loss=min_loss=0
while i<n-1 and j<n:
    if stock_price[i]<stock_price[j]:
        profit= stock_price[j]-stock_price[i]
        j+=1
        max_profit=max(profit,max_profit)
    else:
        i+=1
        j+=1

print(max_profit)

#to find min loss in case of no profits and also the buy and sell time cost during max profit

def stocks(stock_prices):
    buy=stock_prices[0]
    sell=stock_prices[1]
    max_profit=sell-buy

    for i in range(1,len(stock_prices)):
        curr_profit=stock_prices[i]-buy

        if curr_profit>max_profit:
            max_profit=curr_profit
            sell=stock_prices[i]

        if buy>stock_prices[i]:
            buy=stock_prices[i]
            
    return sell-max_profit, sell

print(stocks(stock_price))