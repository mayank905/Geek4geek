# User function Template for python3

class Solution:
    def secondSmallest(self, S, D):
        # code here
        num = [''] * D
        for i in range(D-1,-1,-1):
            if i==0:
                num[i]=str(S)
            else:
                cur=min(9,S-1)
                num[i]=str(cur)
                S-=cur

        i = D - 2
        while i >= 0:
            if int(num[i]) < 9:
                num[i] = str(int(num[i]) + 1)
                num[i + 1] = str(int(num[i+1]) - 1)
                break
            else:
                i -= 1
        if i < 0:
            return -1
        str1 = ''
        return (str1.join(num))


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, D = map(int, input().strip().split(" "))

        ob = Solution()
        print(ob.secondSmallest(S, D))
# } Driver Code Ends