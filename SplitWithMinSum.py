class Solution:
    def splitNum(self, num: int) -> int:
        number=list(str(num))
        number.sort(reverse=True)
        num1=''
        num2=''
        for i,element in enumerate(number):
            if i%2==0:
                num1=element+num1
            else:
                num2=element+num2
        sum1=int(num1)+int(num2)
        return sum1
if __name__ == '__main__':
    G=6887
    obj = Solution()
    ans = obj.splitNum(G)
    print(ans)