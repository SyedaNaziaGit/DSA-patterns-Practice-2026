'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. 
You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        #“the grid is like a graph. 
        # '1'-increment the island count and run DFS to mark all connected land as visited. 
        # This ensures each island is counted once. 
        # Time complexity is O(m × n).
        #len of matrix ie, row and col- grid
        rows = len(grid)#m
        cols = len(grid[0])#n
        islands = 0
        #using dfs- depth first seach algo to find the connected components
        def dfs(m,n):
            if m <0 or m>= rows or n <0 or n>=cols or grid[m][n]=="0":
                return 
            #marking the visited components in the grid
            grid[m][n] ="0"
            #explore  all 4 directions
            dfs(m+1,n)
            dfs(m-1,n)
            dfs(m,n+1)
            dfs(m,n-1)
            #traversing through grid to check if island is visited
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == "1":
                        islands += 1
                        dfs(r,c)
        return islands