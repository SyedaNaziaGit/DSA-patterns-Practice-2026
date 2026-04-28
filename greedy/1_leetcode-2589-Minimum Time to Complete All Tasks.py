'''
There is a computer that can run an unlimited number of tasks at the same time. You are given a 2D integer array tasks where tasks[i] = [starti, endi, durationi] indicates that the ith task should run for a total of durationi seconds (not necessarily continuous) within the inclusive time range [starti, endi].
You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.
Return the minimum time during which the computer should be turned on to complete all tasks.
Example 1:
Input: tasks = [[2,3,1],[4,5,1],[1,5,2]]
Output: 2
Explanation: 
- The first task can be run in the inclusive time range [2, 2].
- The second task can be run in the inclusive time range [5, 5].
- The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
The computer will be on for a total of 2 seconds.
Example 2:
Input: tasks = [[1,3,2],[2,5,3],[5,6,2]]
Output: 4
Explanation: 
- The first task can be run in the inclusive time range [2, 3].
- The second task can be run in the inclusive time ranges [2, 3] and [5, 5].
- The third task can be run in the two inclusive time range [5, 6].
The computer will be on for a total of 4 seconds.
'''

from typing import List
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        #sorting tasks  by their end time
        tasks.sort(key=lambda x:x[1])
        #finding maximum end time
        max_end =  max(e for _,e,_ in tasks)
        #storing time points which are already taken - used
        used = [0] * (max_end+1)
        total_min_time = 0
        # iterating through every task
        for start,end,duration in tasks:
            #finding how many time points already taken
            already = sum(used[start:end+1])
            #remaining time points
            remaining = duration - already
            #if not enough time - adding more time points from right (end-> left)
            t = end
            while remaining > 0:
                if used[t] == 0:
                    used[t] = 1
                    total_min_time += 1
                    remaining -= 1
                t -= 1
        return total_min_time

s = Solution()    
tasks = [[1,3,2],[2,5,3],[5,6,2]]
print(s.findMinimumTime(tasks))#op =  4