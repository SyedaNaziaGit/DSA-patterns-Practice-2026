'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

from typing import  List
from collections import  deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        #initialize
        for r in range(rows):
            for c in range(cols):
                #if orange is rotten
                if grid[r][c] == 2:
                    queue.append((r,c))
                #getting all fresh oranges
                elif grid[r][c] == 1:
                    fresh += 1
        #edge case - if no fresh oranges are present
        if fresh == 0:
            return 0
        #minutes required
        minutes = 0
        #defining the 4 directions 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        #iterating through breath first search to get the minutes
        while queue:
            size = len(queue)#getting the length of queue
            rotten = False
            #iterating
            for _ in range(size):
                #remove from front as this orange will infect neighbour
                r,c = queue.popleft()
                #exploring 4 directions using the directions we have defined earlier
                for dr,dc in directions:
                    #check up down, left and right
                    nr,nc = r + dr, c + dc
                    #validating oranges if fresh then make it rotten as it will be neighbours
                    if 0<=nr < rows and 0<=nc<cols and grid[nr][nc] == 1:
                        #if fresh then make it rotten
                        grid[nr][nc] = 2
                        #also append this in queue
                        queue.append((nr,nc))
                        #now remove count of fresh
                        fresh -= 1
                        rotten = True
            if rotten:
                minutes += 1
                        
        return minutes if fresh == 0 else -1
s= Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.orangesRotting(grid))#op - 4