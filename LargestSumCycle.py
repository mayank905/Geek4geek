# User function Template for python3


class Solution():
    def largestSumCycle(self, N, Edge):
        #your code goes here
        cycleSum=-1
        visited=set()
        for i in range(N):
            if i in visited:
                continue
            else:
                cur=i
                currentSum=0
                stack=[]
                while Edge[cur]!=-1 and Edge[cur] not in visited:
                    cur=Edge[cur]
                    stack.append(cur)
                    visited.add(cur)
                if Edge[cur]==-1:
                    currentsum=0
                else:
                    while stack and stack[-1] !=Edge[cur]:
                        currentSum+=stack[-1]
                        stack.pop()
                    if not stack:
                        continue
                    currentSum += stack[-1]
                    stack.pop()
                    cycleSum=max(cycleSum,currentSum)
        return cycleSum


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        print(Solution().largestSumCycle(N, Edge))
# } Driver Code Ends