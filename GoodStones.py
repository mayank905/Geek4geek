# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

def gudbad(arr, n, dp, index):
    if index < 0 or index >= n:
        return 1
    if dp[index][0] != -1:
        return dp[index][0]
    else:
        if dp[index][1] == True:
            return 0
        dp[index][1] = True
        dp[index][0] = gudbad(arr, n, dp, index + arr[index])
        return dp[index][0]


class Solution:
    def goodStones(self, n, arr) -> int:
        # code here
        dp = [[-1, False] for i in range(n)]
        count = 0
        for i in range(n):

            if gudbad(arr, n, dp, i):
                count += 1
        return count


# {
# Driver Code Starts.

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        obj = Solution()
        print(obj.goodStones(n, arr))

# } Driver Code Ends