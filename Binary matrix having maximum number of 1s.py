# User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        max1 = [0, N]
        for i in range(N):
            if mat[i][max1[1] - 1] == 1:
                for j in range(max1[1] - 1, -1, -1):
                    if mat[i][j] == 0:
                        max1[1] = j + 1
                        max1[0] = i
                        break
        if max1[1] == N:
            return [-1, -1]
        else:
            return [max1[0], N - max1[1]]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob = Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends