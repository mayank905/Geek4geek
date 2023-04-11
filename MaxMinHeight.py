# User function Template for python3

def check(target, k, a, n, w, start):
    i = a.index(start)
    count=0
    while (count<n):
        max1 = 0
        w1 = w
        while (w1 > 0 and count < n):
            w1 -= 1
            if a[i]>target:
                i=(i+1)%n
                count+=1
                continue
            if (target - a[i]) <= k:
                max1 = max(max1, target - a[i])
                i=(i+1)%n
                count+=1
            else:
                return False
            if i==0:
                break
        k = k - max1
    return True


class Solution():
    def maximizeMinHeight(self, n, k, w, a):
        # your code goes here
        start = min(a)
        min1=start
        end = max(a) + k
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if check(mid, k, a, n, w, min1):
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

for _ in range(int(input())):
    n, k, w = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(Solution().maximizeMinHeight(n, k, w, arr))

# } Driver Code Ends