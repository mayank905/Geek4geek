# User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


def aftersum(root):
    if root.left == None and root.right == None:
        return root.data
    min1 = 10 ** 6
    if root.left != None:
        min1 = min(root.data + aftersum(root.left), min1)
    if root.right != None:
        min1 = min(root.data + aftersum(root.right), min1)
    return min1


def find(root, target, tillsum):
    if not root:
        return -1
    if root.data == target:
        as1=10**6
        if root.left != None:
            as1 = min(as1,aftersum(root.left))
        if root.right != None:
            as1 = min(as1,aftersum(root.right))
        if as1==10**6:
            return tillsum
        else:
            return tillsum - as1
    elif root.data > target:
        return find(root.left, target, tillsum + root.data, )
    else:
        return find(root.right, target, tillsum + root.data)


class Solution:
    def maxDifferenceBST(self, root, target):
        # code here
        return find(root, target, 0)


# {
# Driver Code Starts
# Initial Template for Python 3
class Node:
    """ Class Node """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        # tree.traverseInorder(root)
        target = int(input())

        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends