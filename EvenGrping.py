import math
from math import log2


def samegrp(A, B):
    ans1 = math.floor(int(log2(A)))
    ans2 = math.floor(int(log2(B)))
    if ans1 == ans2:
        return True
    else:
        return False


class Solution:
    def evenGrouping(self, n, arr):
        # code here
        set1 = set()
        if n == 1:
            return 1
        condition = True
        i = 1
        prev = 0
        while prev < n - 1:
            if samegrp(arr[prev], arr[i]):
                arr.pop(i)
                arr.pop(prev)
                if prev == 0:
                    i = 1
                    n -= 2
                else:
                    prev = prev - 1
                    i =prev+1
                    n -= 2
            else:
                prev += 1
                i += 1
        ans = len(arr)
        return ans

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.evenGrouping(n, arr)
        print(ans)
        tc -= 1