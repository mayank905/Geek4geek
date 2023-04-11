from typing import List


class Solution(object):
    def minimizeSum(self, nums: List[int]) -> int:
        maxnum=nums[0]
        minnum=nums[0]
        for i in range(1,len(nums)):
            maxnum=nums[i] | maxnum
            minnum=min(minnum,nums[i])
        if minnum>1:
            return 1
        binary=bin(maxnum)
        binary=binary[2:]
        binary=binary[::-1]
        for i in range(len(binary)):
            if binary[i]=='0':
                return 2**i
        return maxnum+1




if __name__ == '__main__':
        num=[4,32,16,8,8,75,1,2]
        obj = Solution()
        ans = obj.minimizeSum(num)
        print(ans)