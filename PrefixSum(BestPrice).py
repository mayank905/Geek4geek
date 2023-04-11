from typing import List


class Solution:
    def bestPrice(self, n: int, price: List[List[int]], k: int, q: int, queries: List[List[int]]) -> List[int]:
        # code here
        min1 = 10 ** 6
        max1 = -1
        for l, r in price:
            min1 = min(l, min1)
            max1 = max(r, max1)
        list1 = [0] * (max1 + 2)
        for l, r in price:
            list1[l] += 1
            list1[r + 1] -= 1

        for i in range(min1, max1 + 1):
            list1[i] += list1[i - 1]

        for i in range(min1, max1 + 1):
            if list1[i] >= k:
                list1[i] = 1
            else:
                list1[i] = 0

        for i in range(min1,max1 + 1):
            list1[i] += list1[i - 1]

        ans = []
        for l, r in queries:
            r = min(max1, r)
            if l>max1:
                ans.append(0)
            else:
                count = list1[r] - list1[l - 1]
                ans.append(count)
        return ans


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        price = IntMatrix().Input(n, 2)

        k = int(input())

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.bestPrice(n, price, k, q, queries)

        IntArray().Print(res)