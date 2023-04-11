from typing import List


# class Solution:
#     def minimumTime(self, time: List[int], totalTrips: int) -> int:
#         time.sort()
#         prevtime=10**7
#         maxtime=totalTrips*time[0]+1
#         curTrip=totalTrips
#         while True:
#             if curTrip<totalTrips:
#                 break
#             else:
#                 prevtime=maxtime
#                 maxtime-=1
#                 curTrip=0
#                 for element in time:
#                     curTrip+=maxtime//element
#                     if curTrip>totalTrips:
#                         break
#                     else:
#                         continue
#
#
#         return prevtime
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        left, right = 1, min(time) * totalTrips

        def timeEnough(given_time):
            actual_trips = 0
            for t in time:
                actual_trips += given_time // t
            return actual_trips >= totalTrips

        while left < right:
            mid = (left + right) // 2
            if timeEnough(mid):
                right = mid
            else:
                left = mid + 1
        return left
if __name__ == '__main__':
    array=[2]
    k=1
    obj = Solution()
    ans = obj.minimumTime(array,k)
    print(ans)