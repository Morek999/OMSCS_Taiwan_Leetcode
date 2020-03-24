""" 
277. Find the Celebrity
https://leetcode.com/problems/find-the-celebrity/
Time complexity: O()
Space complexity: O()
 """

from typing import List
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celeb = 0
        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
        if self.isCelebrity(celeb):
            return celeb
        return -1

    def isCelebrity(self, candidate):
        for i in range(self.n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return False
        return True
        
