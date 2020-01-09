
'''
Idea: Originally I just used two for loop to iterate every possibility and keep updating the max profit, which is O(n^2) and brutal force passed for C++. 
Then I came up using one for loop to keep updating local minimum price(min_price = min(min_price, price[i]) and maximum profit should be equal to either 
previous maximum profit or the current price minus the local minimum price. (max_profit = max(max_profit, price[i] - min_price). 
In the end just output the maximum profit.

Time Complexity: O(n) since we only need one for loop to iterate through the prices list
Space Complexity: O(1) since we only need two variables to record min_price and max_profit 

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: ## check corner case
            return 0
        min_price = prices[0] ## define the initial value for local minimum price
        max_profit = 0 ## define initial value for maximum profit
        for i in range(1,len(prices)): ## use a for loop to iterate the prices list
            min_price = min(min_price,prices[i]) ## update local minimum price
            max_profit = max(max_profit,prices[i] - min_price) ## update the maximum profit
            
        return max_profit