class Solution:
    def noConseBits(self, n: int) -> int:
        # code here
        binary = bin(n)
        binary = binary[2:]
        str1=''
        count = 0
        for i, bit in enumerate(binary):
            if bit == '1':
                count += 1
                if count == 3:
                    str1 += '0'
                    count = 0
                else:
                    str1+='1'
            else:
                count=0
                str1+='0'
        return int(str1, 2)


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        obj = Solution()
        res = obj.noConseBits(n)

        print(res)

# } Driver Code Ends