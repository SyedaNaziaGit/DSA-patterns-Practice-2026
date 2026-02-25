'''
You are given a list schedule where
schedule[i] represents the working intervals of the i-th employee.
Each employee’s intervals are:
Sorted
Non-overlapping
Return the list of finite intervals representing common free time across all employees.
Example:
Input:
[[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output:
[[3,4]]
'''
from typing import List
class Solution:
    def employeeFreeTime(self,schedule:List[List[int]])->List[int]:
        #using merge interval pattern
        #Combine all employees’ intervals into one list.- i.e, flatten
        #import pdb;pdb.set_trace();
        intervals = [interval for employee in schedule for interval in employee]        
        #sort by start time
        intervals.sort(key=lambda x:x[0])
        #Merge overlapping intervals.
        merged = [intervals[0]]
        for start,end in intervals[1:]:
            last_end = merged[-1][1]
            if start<= last_end:
                merged[-1][1]=max(last_end,end)
            else:
                merged.append([start,end])
        #finding the gaps between merged intervals will be common free time.
        free_time = []
        for i in range(1,len(merged)):
            free_time.append([merged[i-1][1],merged[i][0]])
        return free_time
s = Solution()
schedule =  [[[1,2],[5,6]],[[1,3]],[[4,10]]]
print(s.employeeFreeTime(schedule))
#op - [[3,4]]