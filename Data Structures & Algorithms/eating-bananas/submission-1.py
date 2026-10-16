class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)

        def isPileFinished(x):
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i]/x)
                if count > h:
                    return False
            return count <= h

        l, r = 1, maxSpeed
        while l < r:
            mid = (l + r)// 2
            if isPileFinished(mid):
                r = mid
            else:  #0,1,2,3,4
                l = mid + 1
        #they merge at same l = r which is the answer
        return r
