""" 
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        L = len(self.arr)
        if L % 2:
            return self.arr[L//2]
        else:
            return (self.arr[L//2] + self.arr[(L//2) - 1]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        
