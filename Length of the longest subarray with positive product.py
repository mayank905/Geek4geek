# User function Template for python3


class Solution:
    def maxLength(self, arr, n):
        # code here
        maxlength = 0
        length = 0
        curProduct = 1
        neg = 0
        pos = 0
        plus=True
        for i in range(n):
            curProduct *= arr[i]
            if curProduct == 0:
                if neg and neg % 2 == 1:
                    maxlength = max(maxlength, length - pos)
                neg = 0
                pos = i+1
                plus=True
                curProduct = 1
                length = 0
            else:
                if curProduct > 0:
                    if not plus:
                        neg+=1
                    plus=True
                    length += 1
                    maxlength = max(length, maxlength)
                else:
                    if plus:
                        plus=False
                        neg += 1
                        if neg == 1:
                            pos = i + 1 - pos
                    length += 1
        if neg and neg % 2 == 1:
            maxlength = max(maxlength, length - pos)
        return maxlength


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.maxLength(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends