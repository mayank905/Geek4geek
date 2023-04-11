class Solution:
    def saveFlowers(self, n, arr, s):
        # code here
        list1=[int(x) for x in s]
        output=0
        index=-1
        if list1[0]==1:
            output=arr[0]
        else:
            index=0
        for i in range(1,n):
            if list1[i]==1:
                if list1[index]==0 and arr[index]>arr[i] and index!=-1:
                    list1[index]=1
                    list1[i]=0
                    output += arr[index]
                    index=i

                else:
                    output+=arr[i]
            else:
                index=i
        return output
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().split()))
        s = input()
        ob = Solution()
        ans = ob.saveFlowers(n, arr, s)
        print(ans)
        tc -= 1