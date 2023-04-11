# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
from collections import defaultdict

class Solution:
    def removeReverse(self, S):
        #code here
        a={}
        for i in S:
            a[i]=a.get(i,0)+1
        s=list(S)
        startlast=-1;endlast=len(s);i=0;flag=True
        while i>startlast and i<endlast:
            if flag:
                if a[s[i]]>1:
                    a[s[i]]-=1
                    s[i]=-1
                    startlast=i
                    i=endlast-1
                    flag=False
                else:
                    i+=1
            else:
                if a[s[i]]>1:
                    a[s[i]]-=1
                    s[i]=-1
                    endlast=i
                    i=startlast+1
                    flag=True
                else:
                    i-=1
        if flag:
            return ''.join([i for i in s if i!=-1])
        else:
            return ''.join([s[i] for i in range(len(s)-1,-1,-1) if s[i]!=-1])
# class Solution:
#     def removeReverse(self, S):
#         # code here
#         i = 0
#         j = len(S)-1
#         index=[]
#         fdict = defaultdict(int)
#         rev=False
#         while S and i <= j:
#             if not rev:
#                 if S[i] in fdict:
#                     if fdict[S[i]]>i:
#                         index.append(i)
#                     else:
#                         index.append(fdict[S[i]])
#                         fdict[S[i]] = i
#                     rev=True
#                 else:
#                     fdict[S[i]] = i
#                 i += 1
#             else:
#                 if S[j] in fdict:
#                     if fdict[S[j]]<j:
#                         index.append(j)
#                     else:
#                         index.append(fdict[S[j]])
#                         fdict[S[j]]=j
#                     rev=False
#                 else:
#                     fdict[S[j]] = j
#                 j-=1
#         index.sort()
#         count=0
#         for ind in index:
#             ind=ind-count
#             S=S[:ind]+S[ind+1:]
#             count+=1
#         if rev:
#             return S
#         else:
#             return S[::-1]
#


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)

# } Driver Code Ends
