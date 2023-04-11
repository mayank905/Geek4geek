# User function Template for python3

class Solution:
    def endPoints(self, matrix, m, n):
        ##code here
        cord = []
        i, j = 0, 0
        x, y = 0, 0
        cur = 'r'
        while 0 <= j < n and 0 <= i < m:
            x, y = i, j
            if cur == 'r':
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                    i = i + 1
                    cur = 'd'
                else:
                    j += 1
                continue

            if cur == 'd':
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                    j -= 1
                    cur = 'l'
                else:
                    i += 1
                continue

            if cur == 'l':
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                    i = i - 1
                    cur = 'u'
                else:
                    j -= 1
                continue

            if cur == 'u':
                if matrix[i][j] == 1:
                    matrix[i][j] = 0
                    j = j + 1
                    cur = 'r'
                else:
                    i -= 1

        cord.append(x)
        cord.append(y)
        return cord


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix, r, c)
        print('(', ans[0], ', ', ans[1], ')', sep='')

# } Driver Code Ends