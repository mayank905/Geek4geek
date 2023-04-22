# User function Template for python3
def count(N, nums, k):
    d = {0: 1}
    ans = 0
    cur = 0
    sum = 0
    for i in range(N):
        if nums[i] < k:
            sum -= 1
            if sum in d:
                cur -= d[sum]
        else:
            if sum in d:
                cur += d[sum]
            sum += 1
        ans += cur
        if sum in d:
            d[sum] += 1
        else:
            d[sum] = 1
    return ans


class Solution:
    def countSubarray(self, N, A, M):
        # code here
        a = count(N, A, M)
        b = count(N, A, M + 1)
        return a - b


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