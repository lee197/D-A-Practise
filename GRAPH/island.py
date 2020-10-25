class Solution:

  def __init__(self, grid):
    self.grid = grid

  def numIslands(self):
    counter = 0
    for i in range(len(self.grid)):
      for j in range(len(self.grid[0])):
        if self.grid[i][j] == '1':
          counter += 1
          sinkIsland(self.grid, i, j)
    return counter

  def __findNeighbour(sr,sc,grid):
    rowLen = len(grid)
    colLen = len(grid[0])
    res = []
    if sr-1 >= 0 and sc < colLen and grid[sr-1][sc] == 1:
      res.append((sr-1,sc))
    if sr < rowLen and sc-1 >= 0 and grid[sr][sc-1] == 1:
      res.append((sr,sc-1))
    if sr+1 < rowLen and sc < colLen and grid[sr+1][sc] == 1:
      res.append((sr+1,sc)) 
    if sr < rowLen and sc+1 < colLen and grid[sr][sc+1] == 1:
      res.append((sr,sc+1)) 
    return res

def sinkIsland(grid, r, c):
    if grid[r][c] == '1':
      grid[r][c] = '0'
    else:
      return
    if r + 1 < len(grid):
      sinkIsland(grid, r + 1, c)
    if r - 1 >= 0:
      sinkIsland(grid, r - 1, c)
    if c + 1 < len(grid[0]):
      sinkIsland(grid, r, c + 1)
    if c - 1 >= 0:
      sinkIsland(grid, r, c - 1)