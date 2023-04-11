from collections import defaultdict
class Solution:
    def makePermutation(self, n, arr):
        # code here
        di=defaultdict(int)
        set1=set()
        for i in range(1,n+1):
            set1.add(i)
        operation=n
        for i in range(n):
            if 1<=arr[i]<=n:
                if arr[i] in set1:
                    set1.remove(arr[i])
                    operation-=1
                if arr[i] in di:
                    del di[arr[i]]

            else:
                num=arr[i]-1
                while 1<=arr[i]%num<=n:
                    val=arr[i]%num
                    if val in set1:
                        di[val]+=1
                    num-=1
        count=operation
        for element in set1:
            if di[element]==operation:
                continue
            elif di[element]>=1:
                count-=1
            else:
                return -1
        if count>=operation-1:
            return operation
        else:
            return -1
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.makePermutation(n, arr)
        print(ans)
        tc -= 1
