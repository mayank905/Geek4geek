# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:14:29 2023

@author: may9a
"""

#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        lengthM=len(B)
        length=len(A)
        index=0
        match=False
        for i in range(length):
            if A[i:]==B[:length-i]:
                index=i
                match=True
                break
        if not match:
            return -1
        cur=index
        if index==0:
            count=0
        else:
            count=1
        for j in range(lengthM):
            
            if B[j]==A[cur]:
                index+=1
                cur=index%length
                if cur==0:
                    count+=1
                continue
            else:
                return -1
        if cur>0:
            count+=1
        return count
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends