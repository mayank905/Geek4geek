class Solution:
    def totalSubarrays(self, n, x, arr):
        # code here
        left = 0
        right = 0
        count = 0
        xcounter = 0
        boool = True
        while boool:
            while left < n and arr[left] != x :
                left += 1
                right += 1
            if left < n:
                # count += 1
                right += 1
                xcounter += 1
            else:
                boool = False
                break

            while right < n and (x & arr[right] == x):
                if arr[right] == x:
                    xcounter += 1
                right += 1
                count += 1
            if right <= n:
                while (xcounter != 0) and (left < right):
                    if arr[left] == x:
                        xcounter -= 1
                    left += 1
                    count += 1

            if right == n:
                boool = False
        return count
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = map(int,input().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.totalSubarrays(n, x, arr)
        print(ans)
        tc -= 1