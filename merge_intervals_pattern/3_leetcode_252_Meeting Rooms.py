'''
You are given an array of meeting time intervals where
intervals[i] = [start_i, end_i].
Determine if a person could attend all meetings.
Example 1
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation:
Meeting [0,30] overlaps with [5,10].
Example 2
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation:
No overlapping meetings.
'''
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #using merge interval pattern
        #sort the intervals with start time 
        intervals.sort(key=lambda x:x[0])
        #compare each meeting with the previous end time if overlap: false else :true
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
s = Solution()
intervals = [[0,30],[5,10],[15,20]] #False
intervals = [[7,10],[2,4]]#True
print(s.canAttendMeetings(intervals))
#Time Complexity - O(nlogn)- due to sorting  and Space Complexity - O(1)