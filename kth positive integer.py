from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        length=arr[-1]
        index=0
        count=0
        n=len(arr)
        for i in range(1,2*length):
            if index<n and arr[index]==i:
                index+=1
            else:
                count+=1
                if count==k:
                    return i
if __name__ == '__main__':
    array=[1,2,3,4]
    k=2
    obj = Solution()
    ans = obj.findKthPositive(array,k)
    print(ans)