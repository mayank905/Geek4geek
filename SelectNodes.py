# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:14:31 2023

@author: may9a
"""
#User function Template for python3
from collections import defaultdict
count=0
def dfs(adj,index,visited):
    global count
    visited[index]=1
    select=False
    for element in adj[index]:
        if visited[element]==0 and dfs(adj,element,visited)==False:
            select=True
    if select:
        count+=1
    return select
    
class Solution:
    def countVertex(self, N, edges):
        #code here
        global count
        adj=defaultdict(list)
        for i in range(N-1):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        
        visited=[0]*(N+1)
        dfs(adj,1,visited)
        return count
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        edges=[]
        for _ in range(N-1):
            arr = list(map(int,input().split()))
            edges.append(arr)

        ob = Solution()
        print(ob.countVertex(N, edges))
# } Driver Code Ends
