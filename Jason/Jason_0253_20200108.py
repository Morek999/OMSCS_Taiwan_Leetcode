
'''
My first version solution but only passed like half of the tesing case, but I am too busy to finish this question so I need to peek the answer QQ
You can see it in my C++ answer, I will update all of my code tomorrow....

Idea: First sort the meeting intervals by the starting time and we allocate a room by the order of the meeting.
If a meeting is done when a new meeting comes, then we can use the existing room.
If a meeting is not done, then we need to allocate another room.
The implementation can be done by using the min-heap and the key of the min-heap is the ending time of the meeting.
Since the min-heap will always put the earliest ending meeting room on the top, we simply need to check if at that time we can use that room

Time complexity is O(NlogN) since sorting takes NlogN and in the worst case, all N meetings will collide with each other, we will have N extract-min 
operations since extract-min operation on a heap takes O(logN), so the overall time complexity if O(NlogN).
Space complexity is O(N) since we need to create a heap to keep all the meeting room in the worst case
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        minheap = [] ## define minheap to record the room
        intervals.sort(key = lambda x: x[0]) ## sorting by the meeting starting time
        
        heapq.heappush(minheap,intervals[0][1]) ## first meeting we definitely need to allocate 
                                                ## a room
        
        for i in intervals[1:]: ## iterate from the second meeting interval to the end

            ## If the meeting is going to end before the next meeting comes, 
            ## assign that room to this meeting.
            
            if minheap[0] <= i[0]:
                heapq.heappop(minheap) 

            ## Else, assign a new room by push the end time of this meeting to the minheap
            ## And if an old room is allocated, then also we have to add to the heap with 
            ## updated end time.
            heapq.heappush(minheap, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(minheap)
