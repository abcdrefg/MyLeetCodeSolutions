
def maxProfit(prices) -> int:
    profit = 0
    got_stock = False
    price_bought = 0
    prices_size = len(prices)
    for i in range(prices_size):
        if (got_stock):
            if i + 1 == prices_size:
                profit = profit + prices[i] - price_bought
                break
            if i == prices_size - 2:
                if prices[i] < prices[i + 1]:
                    profit = profit + prices[i + 1] - price_bought
                    break
                profit = profit + prices[i] - price_bought
                break
            if prices[i] < prices[i + 1]:
                continue
            got_stock = False
            profit = profit + prices[i] - price_bought
            continue
        if i+1 == prices_size:
            break
        if prices[i] < prices[i+1]:
            got_stock = True
            price_bought = prices[i]
    return profit

maxProfit([1])