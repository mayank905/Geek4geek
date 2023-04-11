from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findRoot(inorder,postorder):
    if len(inorder)==0:
        return None
    if len(inorder)==1:
        return TreeNode(inorder[0])
    val=postorder[-1]
    node=TreeNode(val)
    postorder.pop(-1)
    ind=inorder.index(val)
    leftinorder=inorder[:ind]
    rightinorder=inorder[ind+1:]
    length=len(leftinorder)
    leftpostorder=postorder[:length]
    rightpostorder=postorder[length:]
    node.left=findRoot(leftinorder,leftpostorder)
    node.right=findRoot(rightinorder,rightpostorder)
    return node


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node=findRoot(inorder,postorder)
        return node
if __name__ == '__main__':
        obj = Solution()
        I=[2,1]
        P=[2,1]
        ans = obj.buildTree(I,P)
        print(ans)