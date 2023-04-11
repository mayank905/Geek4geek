from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""


def findPrime(x, arr):
    if x in arr:
        return x
    else:
        next = x + 1
        prev = x - 1
        while prev > 1 and next <= 10 ** 4:
            if prev in arr:
                return prev
            elif next in arr:
                return next
            else:
                next += 1
                prev -= 1
        if prev <= 1:
            return 2


def sieve(x, y):
    numbers = [i for i in range(x, y + 1)]
    i = 0

    while i < len(numbers):

        if numbers[i] is not None:
            for j in range(i + numbers[i], len(numbers), numbers[i]):
                numbers[j] = None
        i += 1
    set1 = set()
    for n in numbers:
        if n is not None:
            set1.add(n)
    return set1


# Driver program
boolean = True


class Solution:
    def primeList(self, head: Optional['Node']) -> Optional['Node']:
        # code here
        result = head
        global boolean
        global lst
        if boolean:
            starting_range = 2
            ending_range = 10 ** 4
            lst = sieve(starting_range, ending_range)
            boolean = False
        while head.next != None:
            p = findPrime(head.data, lst)
            head.data = p
            head = head.next
        p = findPrime(head.data, lst)
        head.data = p
        return result

# {
# Driver Code Starts
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next
    print()


def inputList():
    n = int(input())  # lenght of link list
    data = [int(i) for i in input().strip().split()]  # all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1, n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        head = inputList()

        obj = Solution()
        res = obj.primeList(head)

        printList(res)

# } Driver Code Ends