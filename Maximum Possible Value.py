# User function Template for python3
class Solution:
    # def maxPossibleValue(self, N, A, B):
    #     # code here
    #     lis = list(zip(A, B))
    #     lis.sort(reverse=True,key=lambda i: (i[1],i[0]))
    #     max1=[0,0]
    #     sq = list(map(lambda x: x[1]//4, lis))
    #     re = list(map(lambda x: x[1]%4, lis))
    #     sum1=0
    #     count=0
    #     pending=0
    #     for i in range(N):
    #         if sq[i]>0:
    #             sum1+=sq[i]*4*lis[i][0]
    #         if re[i]>=2:
    #             count+=1
    #             if count%2==0:
    #                 pending+=2*lis[i][0]
    #                 sum1+=pending
    #                 pending=0
    #             else:
    #                 pending=2*lis[i][0]
    #     return sum1
    def maxPossibleValue(self, N, A, B):

        mn = int(1e9)

        count = 0

        res = 0

        for i in range(N):

            if B[i] > 1:
                rect_pairs = B[i] // 2

                res += 2 * (rect_pairs * A[i])

                mn = min(mn, A[i])

                count += rect_pairs

        if count % 2 != 0:
            res -= 2 * mn

        return res

# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends