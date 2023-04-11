# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:30:08 2023

@author: may9a
"""


# User function Template for python3
# def distinct(r, g, b, i, prev):
#     if i < 0:
#         return 0
#     else:
#         if dp[i][prev] != -1:
#             return dp[i][prev]
#         ans = 10 ** 12
#
#         if prev == 0:
#             ans = min(ans, g[i] + distinct(r, g, b, i - 1, 1))
#             ans = min(ans, b[i] + distinct(r, g, b, i - 1, 2))
#         if prev == 1:
#             ans = min(ans, r[i] + distinct(r, g, b, i - 1, 0))
#             ans = min(ans, b[i] + distinct(r, g, b, i - 1, 2))
#         if prev == 2:
#             ans = min(ans, g[i] + distinct(r, g, b, i - 1, 1))
#             ans = min(ans, r[i] + distinct(r, g, b, i - 1, 0))
#
#         dp[i][prev] = ans
#         return ans


class Solution:
    def distinctColoring(self, N, r, g, b):
        # code here
        for i in range(1, len(r)):
            r[i] += min(g[i - 1], b[i - 1])
            g[i] += min(r[i - 1], b[i - 1])
            b[i] += min(r[i - 1], g[i - 1])
        return min(r[-1], g[-1], b[-1])

    # def distinctColoring(self, N, r, g, b):
        # code here
        # global dp
        # dp = [[-1 for i in range(3)] for j in range(N)]
        # ans = 10 ** 12
        # for i in range(3):
        #     ans = min(ans, distinct(r, g, b, N - 1, i))
        # return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        r = list(map(int, input().split()))
        g = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ob = Solution()
        print(ob.distinctColoring(N, r, g, b))
# } Driver Code Ends
