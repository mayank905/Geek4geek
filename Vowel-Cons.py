from collections import defaultdict
class Solution:
    def valuableString(self, n, arr):
        # code here
        val=[-10**7 ,""]
        for i in range(n):
            vo=0
            co=0
            for c in arr[i]:
                if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                    vo+=1
                else:
                    co+=1
            diff=abs(co-vo)
            if diff>val[0]:
                val=[diff,arr[i]]
        return val[1]
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().split()))
        ob = Solution()
        ans = ob.valuableString(n, arr)
        print(ans)
        tc -= 1
