from typing import List
from collections import defaultdict


def bestValue(Source, dp, children, Value, sign):
    if dp[Source] == -1:
        if sign == 1:
            mul = 1
            sign = 0
        else:
            mul = -1
            sign = 1
        value = Value[Source - 1] * mul
        if Source not in children:
            dp[Source]=value
            return value
        ans = -10 ** 6
        for element in children[Source]:
            ans = max(ans, value + bestValue(element, dp, children, Value, sign))
        dp[Source] = ans
        return ans
    else:
        return dp[Source]


class Solution:
    def bestNode(self, N: int, A: List[int], P: List[int]) -> int:
        # code here
        dp1 = [-1]*(N + 1)
        dp0 = [-1]*(N + 1)
        children = defaultdict(list)
        level = defaultdict(int)
        for i in range(1, len(P) + 1):
            if P[i - 1] == -1:
                continue
            children[P[i - 1]].append(i)
        ans = -10 ** 6
        dp1[0]=bestValue(1, dp1, children, A, 1)
        ans=dp1[0]
        dp0[0]=bestValue(1, dp0, children, A, -1)
        level[1]=1
        for i in range(1,N+1):
            for element in children[i]:
                level[element]=level[i]+1
        for i in range(1, N + 1):
            if level[i]%2==1:
                ans=max(ans,dp1[i])
            else:
                ans = max(ans,dp0[i])
        return ans


# {
# Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        A = IntArray().Input(N)

        P = IntArray().Input(N)

        obj = Solution()
        res = obj.bestNode(N, A, P)

        print(res)

# } Driver Code Ends