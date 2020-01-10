'''

Idea: this question is essentially fabonacci question. I created an array to improve the efficiency (memorization).
Define an array named mem to record the ways that I can get to position i. Since you can either jump one step or two steps, 
the ways you can get to position i will simply be the summation of the ways at i - 1 and i - 2. In code:

mem[i] = mem[i-1] + mem[i-2]

The initial condition will be n = 1 and 2. When n = 1, then there's only 1 way(1 step). When n = 2, there's two ways(2 or 1 + 1 step).
From n = 2 we can use the for loop and equation above to iterate and build the matrix.
In the end we just need to output mem[n-1]

Time complexity: O(n) since we need to use a for loop n times
Space complexity: O(n) since we created an array to record n values
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: 
            return 1  ## corner case check
        
        mem = [0] *n ## define the list to record n values
        mem[0] = 1
        mem[1] = 2  ## initial condition setup
        
        for i in range(2,n):
            mem[i] = mem[i-1] + mem[i-2] ## find the ways at every postion i
        
        return mem[n-1] 