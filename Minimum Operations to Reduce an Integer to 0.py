import math
def minOp(n):
    a = int(math.log2(n))
    p = 2 ** a
    p1 = 2 ** (a + 1)
    p2 = 2 ** (a - 1)
    if p == n:
        return 1
    else:
        if p < n:
            ans1 = minOp(n - p)
            ans2 = minOp(p1 - n)
        else:
            ans1 = minOp(n - p2)
            ans2 = minOp(p - n)
        ans = 1 + min(ans1, ans2)
        return ans
class Solution:
    def minOperations(self, n: int) -> int:
        a = int(math.log2(n))
        p=2**a
        p1=2**(a+1)
        p2=2**(a-1)
        if p==n:
            return 1
        else:
            if p<n:
                ans1=minOp(n-p)
                ans2=minOp(p1-n)
            else:
                ans1=minOp(n-p2)
                ans2=minOp(p-n)
            ans=1+min(ans1,ans2)
            return ans

if __name__ == '__main__':
    num = 54
    obj = Solution()
    ans = obj.minOperations(num)
    print(ans)