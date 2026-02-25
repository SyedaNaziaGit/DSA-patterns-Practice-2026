'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
'''
from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #using merge interval pattern
        i = j = 0
        result = []
        while i < len(firstList) and j < len(secondList):
            start1,end1 =  firstList[i]
            start2,end2 = secondList[j]
            #intersection
            start = max(start1,start2)
            end = min(end1,end2)
            if start <= end:
                result.append([start,end])
            #else move pointer that ends first
            if end1 < end2:
                i += 1
            else:
                j += 1
        return result
s = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(s.intervalIntersection(firstList,secondList))
#op - [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
firstList = [[1,3],[5,9]]
secondList = []
print(s.intervalIntersection(firstList,secondList))
#op - []