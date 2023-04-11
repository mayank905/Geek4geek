from collections import defaultdict
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        adj=defaultdict(list)
        N=len(edges)
        for i in range(N):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        gset1=set()
        gset2=set()
        for i in range(len(guesses)):
            st1=str(guesses[i][0])+str(guesses[i][1])
            st2=str(guesses[i][1])+str(guesses[i][0])
            if st2 in gset1:
                continue
            else:
                gset2.add(st2)
                gset1.add(st1)
        count=0
        for i in range(N+1):
            mincount=0
            setCount=len(gset1)
            for element in adj[i]:
                st1=str(i)+str(element)
                st2=str(element)+str(i)
                if st1 in gset1:
                    mincount+=1
                    setCount-=1
                    continue
                else:
                    if st2 in gset1:
                        setCount-=1
            cursum=mincount+setCount
            if cursum>=k:
                count+=1
        return count
if __name__ == '__main__':
    edges=[[0,1],[2,0],[0,3],[4,2],[3,5],[6,0],[1,7],[2,8],[2,9],[4,10],[9,11],[3,12],[13,8],[14,9],[15,9],[10,16]]
    guess=[[8,2],[12,3],[0,1],[16,10]]
    k=2
    obj = Solution()
    ans = obj.rootCount(edges,guess,k)
    print(ans)