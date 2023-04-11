from collections import Counter


class Solution(object):
    def minMaxDifference(self, num):
        list1=list(map(int, str(num)))
        maxlist=''
        minlist=''
        n=len(list1)
        bool=True
        for i in range(n):
            if bool:
                if list1[i]==9:
                    maxlist+=str(9)
                    continue
                else:
                    val=list1[i]
                    maxlist += str(9)
                    bool=False
            else:
                if list1[i]==val:
                    maxlist += str(9)
                else:
                    maxlist+=str(list1[i])
        bool=True
        for i in range(n):
            if bool:
                if list1[i]==0:
                    minlist+=str(0)
                    continue
                else:
                    val=list1[i]
                    minlist += str(0)
                    bool = False
            else:
                if list1[i]==val:
                    minlist+=str(0)
                else:
                    minlist += str(list1[i])


        max1=int(maxlist)
        print(max1)
        min1=int(minlist)
        print(min1)
        diff=max1-min1
        return diff





        return list1

if __name__ == '__main__':
        num=90
        obj = Solution()
        ans = obj.minMaxDifference(num)
        print(ans)