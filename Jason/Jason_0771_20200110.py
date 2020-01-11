'''
Idea: the ideas is to use hashset to store the types of the stone and then check every character in S and see if it's in the hashset 
and calculate the total number

Time complexity: O(j+s), where j is the length of J and s is the length of S. Since when we create the set to store the component in J,
we need to iterate through the entire string, which is O(j) operation and add a component to a hashset is O(1) operation.
When we check how many jewels exist, we need to iterate through S and look up in hash set is O(1) operation, so this move is O(s)
so the total complexity is O(j+s)

Space complexity: O(j) since we need to store every jewels in the hash set 

'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(J) == 0 or len(S) == 0:  ## check corner case
            return 0
        
        jewel = set(J) ## create hash set to store the jewels type
        
        ans = 0
        for s in S:
            if s in jewel: ## iterate through the S string and count the number of jewels
                ans += 1
            
        return ans