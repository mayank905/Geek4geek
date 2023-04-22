def check(pos,arr,n,m,c):
    m=m-1
    last=arr[0]
    for i in range(1,n):

        if (arr[i]-last)>pos:
            if m>0:
                m-=1
                last=arr[i]
                continue
            else:
                return False

    return True
class Solution:
    def minimumWaitTime(self, n, m, c, arr):
        # code here
        arr.sort()
        max1=arr[-1]
        min1=0
        while(min1<=max1):
            mid=(min1+max1)//2
            if check(mid,arr,n,m,c):
                max1=mid-1
            else:
                min1=mid+1
        return min1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m, c = map(int,input().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minimumWaitTime(n, m, c, arr)
        print(ans)
        tc -= 1