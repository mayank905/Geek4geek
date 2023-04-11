class Solution:
    def distMoney(self, money: int, children: int) -> int:
        child=[1]*children
        money-=children
        if money<0:
            return -1
        count=0
        for i in range(children):
            amount=min(7,money)
            if amount==7:
                count+=1
            if amount==3:
                if i==children-1:
                    if count==0:
                        continue
                    else:
                        count-=1
                else:
                    money-=1
                    continue
            money-=amount
        if money>0 and count>0:
            count-=1
        return count
if __name__ == '__main__':
    m=17
    c=2
    obj = Solution()
    ans = obj.distMoney(m,c)
    print(ans)