from typing import List
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        a, l, h = 0, len(nums) - 1, len(nums) - 1
        for i in range(len(nums)):
            while 0 <= h and nums[i] + nums[h] > upper:
                h -= 1
            while 0 <= l and nums[i] + nums[l] >= lower:
                l -= 1
            a += h - l - (1 if l < i and i <= h else 0)
        return a // 2
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         length=len(nums)
#         nums.sort()
#         count=0
#         i=0
#         j=length-1
#         while i<j:
#             for k in range(i,length - 1):
#                 if (nums[k] + nums[k + 1]) >= lower:
#                     left = k
#                     break
#             sum1=(nums[left] + nums[j])
#             if lower <= sum1 <= upper:
#                     count+=j-left
#                     i+=1
#             else:
#                 if sum1>upper:
#                     j-=1
#                 elif sum1<lower:
#                     i+=1
#
#
#         return count
if __name__ == '__main__':
        # nums=[0,1,7,4,4,5]
        # lower=3
        # upper=6
        nums=[1,7,9,2,5]
        lower=11
        upper=11
        obj = Solution()
        ans = obj.countFairPairs(nums,lower,upper)
        print(ans)