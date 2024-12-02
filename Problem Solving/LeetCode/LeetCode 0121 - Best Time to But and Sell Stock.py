# LeetCode 121 - Best Time to Buy and Sell Stock
# (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

def maxProfit(prices):
    # Initialize two pointers
    buy = 0  # Pointer 1
    sell = 1  # Pointer 2
    max_profit = 0  # Variable to store the maximum profit encountered

    while sell < len(prices):
        if prices[buy] < prices[sell]:  # Check if the current "buy" price is less than the current "sell" price
            profit = prices[sell] - prices[buy]  # If yes, calculate profit
            if profit > max_profit:  # Update max_profit if the current profit is greater
                max_profit = profit
        else:  # If current buy price is more than sell, update buy pointer to current sell pointer
            buy = sell
        sell += 1   # Move the "sell" pointer to the next day

    return max_profit  # Return the maximum profit found


# Test case: Example array of stock prices
price1 = [7,1,5,3,6,4]
profit1 = maxProfit(price1)
print(profit1)  # Output = 5