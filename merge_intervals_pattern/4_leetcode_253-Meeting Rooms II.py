'''
Given an array of meeting time intervals
intervals[i] = [start_i, end_i],
Return the minimum number of conference rooms required.
Example 1
Input: [[0,30],[5,10],[15,20]]
Output: 2
Explanation:
At time 5, meetings [0,30] and [5,10] overlap → need 2 rooms.
Example 2
Input: [[7,10],[2,4]]
Output: 1
'''
from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #using merge interval pattern 
        #using minheap - priority queue so that it gives the peek  with O(1)(peek) and O(logn) -insert or removal of element
        #A min heap always keeps the smallest element at the top.
        #edge case        
        if not intervals:
            return 0
        #base case
        #sort the  intervals by start time
        intervals.sort(key= lambda x : x[0])
        #using min heap to track end time
        minheap = []
        #adding first meeting to heapq
        heapq.heappush(minheap,intervals[0][1])
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            #if room is free reuse it
            if start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap,end)
        return len(minheap)
s= Solution()
intervals = [[7,10],[2,4]]
intervals = [[0,30],[5,10],[15,20]]
print(s.minMeetingRooms(intervals))