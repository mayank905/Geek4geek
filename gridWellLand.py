from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        res = 0
        while dq:
            r0, c0 = dq.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < n and 0 <= c1 < n and not grid[r1][c1]:
                    dq.append((r1, c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    res = max(res, grid[r1][c1])
        return res - 1

# def call(arr,row,col,dp,rlimit,climit,visited):
#     if row==rlimit or col==climit:
#         return 10**4
#     if dp[row][col]!=-1:
#         return dp[row][col]+1
#     else:
#         if arr[row][col]==1:
#             dp[row][col]=1
#             return 1
#         else:
#             if visited[row][col]==False:
#                 visited[row][col]=True
#                 ans1=call(arr,row+1,col,dp,rlimit,climit,visited)
#                 ans2=call(arr,row-1,col,dp,rlimit,climit,visited)
#                 ans3=call(arr,row,col+1,dp,rlimit,climit,visited)
#                 ans4=call(arr,row,col-1,dp,rlimit,climit,visited)
#                 dp[row][col]=min(ans1,ans2,ans3,ans4)
#
#                 return dp[row][col]+1
#             else:
#                 return 10**4
#
#
#
# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         row=len(grid)
#         col=len(grid[0])
#         dist=-1
#
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j]==0:
#                     dp = [[-1 for m in range(row)] for n in range(col)]
#                     visited = [[False for m in range(row)] for n in range(col)]
#                     dist=max(dist,call(grid,i,j,dp,row,col,visited)-1)
#         return dist
if __name__ == '__main__':
        # G = [[1,0,1],[0,0,0],[1,0,1]]
        # G = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        G=[[1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],[1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,1],[0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],[0,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1],[1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0],[0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0],[1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1],[0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0],[0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0],[0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0],[0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1],[1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0],[1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1],[0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0]]
        obj = Solution()
        ans = obj.maxDistance(G)
        print(ans)