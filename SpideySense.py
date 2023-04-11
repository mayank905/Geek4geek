from collections import deque

class Solution:
    def shortestDistanceFromTheBomb(self, matrix, m, n):
        # code here
        q=deque()
        ans = [row[:] for row in matrix]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'O':
                    ans[i][j] = 10 ** 5
                elif matrix[i][j] == 'B':
                    ans[i][j] = 0
                    q.append([i,j])
                elif matrix[i][j] == 'W':
                    ans[i][j] = -1
        while q :
            row,col=q.popleft()
            loop = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for j, k in loop:
                if 0 <= row + j < m and 0 <= col + k < n and ans[row + j][col + k]>ans[row][col]+1 and ans[row + j][col + k]!=-1:
                    ans[row + j][col + k] = ans[row][col] + 1
                    q.push([row + j,col + k])
        return ans
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        m,n=map(int,input().split())
        matrix=[]
        for _ in range(m):
            matrix.append( [ x for x in input().strip().split() ] )
        ob = Solution()
        result=ob.shortestDistanceFromTheBomb(matrix,m,n)
        for i in result:
            for j in i:
                print(j, end=' ')
            print()