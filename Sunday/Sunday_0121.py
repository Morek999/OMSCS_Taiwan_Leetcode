# NewConcept
# My first thought came with two pointers
# However, after looking into the discussion, I found this questions also belongs to max subarry problem
# Take reference from the following page:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCur, maxSoFar = 0, 0
        for i in range(1, len(prices)):
            maxCur = maxCur + prices[i] - prices[i-1]      
            maxCur = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)
            
        return maxSoFar
        
        
        
