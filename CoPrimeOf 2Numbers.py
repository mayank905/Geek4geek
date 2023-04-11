from typing import List
from collections import defaultdict


prime=[True]*((10**6)+1)
bol=True
pset=[]
def sieve(array):
    array[0]=False
    array[1]=False
    length=len(array)
    for num in range(2,length):
        if array[num]==True:
            pset.append(num)
            iter=num+num
            while iter<length:
                array[iter]=False
                iter+=num

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        global prime
        global bol
        global pset
        if bol:
            sieve(prime)
            bol=False
        indDict=[]
        wholeDict=defaultdict(int)
        leftDict=defaultdict(int)
        for element in nums:
            cur=defaultdict(int)
            for p in pset:
                if p>element:
                    break
                else:
                    j=element
                    while j%p==0:
                        cur[p]+=1
                        wholeDict[p]+=1
                        j=j//p
            indDict.append(cur)
        for i in range(len(nums)-1):
            bol1=False
            count=0
            for element in indDict[i]:
                leftDict[element]+=indDict[i][element]
                wholeDict[element]-=indDict[i][element]
                if wholeDict[element]>0:
                    bol1=False
                    count+=1
                else:
                    bol1=True
            if bol1 and count==0:
                return i+1
        return -1





if __name__ == '__main__':
    array=[4,7,15,8,3,5]
    obj = Solution()
    ans = obj.findValidSplit(array)
    print(ans)