from collections import deque


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List
def chkQuad(node,grid,i,j,size):
    if size==1:
        if grid[i][j]==1:
            node.val=1
            node.isLeaf=1
        else:
            node.val=0
            node.isLeaf=1
        return node
    size=size//2
    topL=Node(-1,-1,None,None,None,None)
    topL=chkQuad(topL, grid, i, j, size)
    topR=Node(-1,-1,None,None,None,None)
    topR=chkQuad(topR, grid, i, j+size, size)
    bottomL=Node(-1,-1,None,None,None,None)
    bottomL=chkQuad(bottomL, grid, i+size, j, size)
    bottomR=Node(-1,-1,None,None,None,None)
    bottomR=chkQuad(bottomR, grid, i+size, j+size,size)
    if topL.isLeaf and topR.isLeaf and bottomL.isLeaf and bottomR.isLeaf:
        if topL.val==topR.val and topR.val==bottomR.val and bottomR.val==bottomL.val:
            node.val=grid[i][j]
            node.isLeaf=1
            return node

    node.val=1
    node.isLeaf=0
    node.topLeft=topL
    node.topRight=topR
    node.bottomLeft=bottomL
    node.bottomRight=bottomR
    return node


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        size=len(grid)
        root=Node(-1,-1,None,None,None,None)
        root=chkQuad(root,grid,0,0,size)
        return root
def createlist(list1,node,anslist):

    list1.append(node)
    while list1:
        node=list1.popleft()
        if not node.isLeaf:
            list1.append(node.topLeft)
            list1.append(node.topRight)
            list1.append(node.bottomLeft)
            list1.append(node.bottomRight)
        if node.isLeaf:
            val1 = 1
        else:
            val1 = 0
        if node.val:
            val2 = 1
        else:
            val2 = 0
        cur = [val1, val2]
        anslist.append(cur)
if __name__ == '__main__':
    num = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    obj = Solution()
    ans = obj.construct(num)
    anslist=[]
    q=deque()
    createlist(q,ans,anslist)
    print(anslist)