""" 
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        self.hasNext()
        nL, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nL[i].getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            nL, i = self.stack[-1]
            if i == len(nL):
                s.pop()
            else:
                if nL[i].isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([nL[i].getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())