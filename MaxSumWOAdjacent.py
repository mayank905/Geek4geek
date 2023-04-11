# User function Template for python3
# import sys
# sys.setrecursionlimit(10**7)
# def findMax(arr, dp, i, n):
#     if i > n - 1:
#         return 0
#     else:
#         if dp[i] != -1:
#             return dp[i]
#         else:
#             sum1 = arr[i] + max(findMax(arr, dp, i + 2, n), findMax(arr, dp, i + 3, n))
#             dp[i] = sum1
#             return dp[i]
#
#
# class Solution:
#
#     def findMaxSum(self, arr, n):
#         # code here
#         dp = [-1] * n
#         ans = findMax(arr, dp, 0, n)
#         ans = max(ans,findMax(arr, dp, 1, n))
#         return ans

class Solution:
	def findMaxSum(self,arr, n):
		a = b = 0
		for num in arr:
		    a, b = b, max(b, a + num)
		return b

# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends