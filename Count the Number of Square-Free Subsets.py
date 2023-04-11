from typing import List
from itertools import combinations
import math

def isSquare(n):
    sq=(int)(math.sqrt(n))
    for i in range(2,sq+1):
        if n%(i**2)==0:
            return False
    return True


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        list1=set()
        for i in range(len(nums)):
            if isSquare(nums[i]):
                list1.add(nums[i])
        ans=0
        for i in range(len(list1)):
            comb = combinations(list1, i+1)
            ans+=len(list(comb))
        return ans

if __name__ == '__main__':
    # num = [26,6,4,27,6,18]
    num = [8,11,17,2,25,29,21,20,4,22]
    obj = Solution()
    ans = obj.squareFreeSubsets(num)
    print(ans)