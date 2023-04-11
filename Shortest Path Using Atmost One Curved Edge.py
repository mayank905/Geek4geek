# User function Template for python3
# from collections import defaultdict
# import heapq
#
# def distance(curve, a, b, strght, curv, visited):
#     if a == b:
#         return 0
#     mins = [0, 10 ** 4]
#     minc = [0, 10 ** 4]
#     dests = 10 ** 4
#     destc = 10 ** 4
#     adjs=[]
#     adjc=[]
#     for i in range(len(strght[a])):
#         if strght[a][i][0] == b:
#             dests = strght[a][i][1]
#             destc = curv[a][i][1]
#         else:
#             if strght[a][i][0] in visited:
#                 continue
#             else:
#                 heapq.heappush(adjs,strght[a][i])
#                 heapq.heappush(adjc,curv[a][i])
#     ans=10**5
#     if not adjs:
#         if dests==10**4:
#             return ans
#         else:
#             if curve:
#                 return dests
#             else:
#                 return destc
#     while ans>10**4:
#         mins=heapq.heappop(adjs)
#         minc=heapq.heappop(adjc)
#         visiteds = visited.copy()
#         visitedc = visited.copy()
#         visiteds.add(mins[0])
#         visitedc.add(minc[0])
#
#         if curve:
#             ans1 = mins[1] + distance(True, mins[0], b, strght, curv, visiteds)
#             ans = min(destc, dests, ans1)
#         else:
#             ans1 = mins[1] + distance(False, mins[0], b, strght, curv, visiteds)
#             ans2 = minc[1] + distance(True, minc[0], b, strght, curv, visitedc)
#             ans = min(destc, dests, ans1, ans2)
#     return ans
#
#
# class Solution:
#     def shortestPath(self, n, m, a, b, edges):
#         strght = defaultdict(list)
#         curv = defaultdict(list)
#         curve = False
#         visited = set()
#         for source, destination, straight, cur in edges:
#             strght[source].append([destination, straight])
#             strght[destination].append([source, straight])
#             curv[source].append([destination, cur])
#             curv[destination].append([source, cur])
#         visited.add(a)
#         return distance(curve, a, b, strght, curv, visited)

from heapq import heappop, heappush
from math import inf


class Solution:
    def dijkstra(self, graph, src):
        n = len(graph)
        dist = [inf] * n
        dist[src] = 0
        heap = [(dist[src], src)]

        while heap:
            d, u = heappop(heap)
            if dist[u] < d:
                continue
            for v, wt in graph[u]:
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heappush(heap, (dist[v], v))
        return dist

    def shortestPath(self, n, m, a, b, edges):
        graph = [[] for _ in range(n)]
        for u, v, w1, _ in edges:
            graph[u - 1].append((v - 1, w1))
            graph[v - 1].append((u - 1, w1))

        dista = self.dijkstra(graph, a - 1)
        distb = self.dijkstra(graph, b - 1)

        res = dista[b - 1]
        for u, v, _, w2 in edges:
            res = min(res, dista[u - 1] + w2 + distb[v - 1])
            res = min(res, distb[u - 1] + w2 + dista[v - 1])

        return res if res != inf else -1
# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)
from heapq import *

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a, b = map(int, input().split())
        edges = []
        for i in range(m):
            edge = list(map(int, input().split()))
            edges.append(edge)

        ob = Solution()
        print(ob.shortestPath(n, m, a, b, edges))
# } Driver Code Ends