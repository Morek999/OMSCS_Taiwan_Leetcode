/*
Please see Jason_0121.py for explanation.
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()){
            return 0;
        }
        int maxprofit = 0 , minprice = prices[0];
        for(int i = 1; i < prices.size(); i++){
            minprice = min(minprice,prices[i]);
            maxprofit = max(maxprofit,prices[i] - minprice);
        }
        return maxprofit;
    }
};