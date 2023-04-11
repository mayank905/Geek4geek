from collections import deque
from typing import List

ans=[]
ind=[False]*2001
def levelOrder(root,index):
    if root.left:
        if ind[index+1]==True:
            ans[index+1].append(root.left.data)
        else:
            ans.append([root.left.data])
            ind[index+1]=True
        levelOrder(root.left,index+1)
    if root.right:
        if ind[index+1]==True:
            ans[index+1].append(root.right.data)
        else:
            ans.append([root.right.data])
            ind[index+1]=True
        levelOrder(root.right,index+1)



class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        global ans
        ans=[]

        if root:
            minians=[root.data]
            ans.append(minians)
            ind[0]=True
            levelOrder(root,0)
            for i in range(1,len(ans)+1):
                if i%2==0:
                    ans[i-1].reverse()
        return ans
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
def buildTree(s):

    ip = s

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == '__main__':
        num=[1,2,'N']
        root = buildTree(num)
        obj = Solution()
        ans = obj.zigzagLevelOrder(root)
        print(ans)