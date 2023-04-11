from collections import defaultdict
class Solution:
    def minimumOperations(self, n, A):
        # code here
        dict1=defaultdict(int)
        bol=True
        for i in range(n):
            if A[i]%3!=0:
                bol=False
                dict1[A[i]%3]+=1
        if bol:
            return 0
        operations=0
        if dict1[2]>0:
            if dict1[1]<dict1[2]:
                operations+=dict1[1]
                dict1[2] = dict1[2] - dict1[1]
                dict1[1]=0
            else:
                operations+=dict1[2]
                dict1[1]=dict1[1]-dict1[2]
                dict1[2]=0
        if dict1[1]!=0:
            if dict1[1]%3==0:
                operations+=(dict1[1]//3)*2
                return operations
            else:
                return -1
        if dict1[2] != 0:
            if dict1[2] % 3 == 0:
                operations += (dict1[2] // 3) * 2
                return operations
            else:
                return -1
        if operations>0:
            return operations
        else:
            return -1
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.minimumOperations(n, arr)
        print(ans)
        tc -= 1