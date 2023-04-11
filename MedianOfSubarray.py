# User function Template for python3
from collections import defaultdict
def median(arr,sor,length):
    global ans
    if length==0:
        return
    tp=tuple(arr)
    if tp in dp:
        return
    dp.add(tp)
    if length % 2 == 0:
        mid = (length // 2) - 1
    else:
        mid = length // 2
    if sor[mid] == M:
        ans += 1
    num = arr[-1][1]
    sor1=sor.copy()
    sor.remove(num)
    num =arr[0][1]
    sor1.remove(num)
    length -= 1
    A=arr[:length]
    A1=arr[1:]
    median(A,sor,length)
    median(A1,sor1,length)
    return

class Solution:
    def countSubarray(self, N, A, M):
        # code here
        global dp
        global ans
        ans=0
        dp=set()
        B=list(enumerate(A))
        sor = sorted(A)
        length = N
        median(B,sor,length)
        return ans



# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, M)
        print(ans)

# } Driver Code Ends