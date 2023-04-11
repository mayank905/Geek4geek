from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        length=len(nums)
        mark=[False]*length
        n1=nums.copy()
        n1=list(enumerate(n1))
        n1.sort(key=lambda x:x[1])
        while n1:
            num=n1[0][1]
            ind=n1[0][0]
            if mark[ind]==False:
                score+=num
                mark[ind]=True
                if ind+1<length:
                    mark[ind+1]=True
                if ind-1>=0:
                    mark[ind-1]=True
            n1=n1[1:]
        return score
if __name__ == '__main__':
    m=[2,3,5,1,3,2]
    obj = Solution()
    ans = obj.findScore(m)
    print(ans)