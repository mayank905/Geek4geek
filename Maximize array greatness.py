from collections import defaultdict
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        small=0
        d=defaultdict(int)
        d[nums[0]]=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                small+=d[nums[i-1]]
            d[nums[i]]+=1
            if small>0:
                count+=1
                small-=1
        return count
if __name__ == '__main__':
    m=[1,3,5,2,1,3,1]
    obj = Solution()
    ans = obj.maximizeGreatness(m)
    print(ans)