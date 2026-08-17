import math

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)
        
        # Impossible case: need at least n-1 full hours for waiting
        if hour <= n - 1:
            return -1
        
        def canReach(speed):
            total = 0
            for i in range(n - 1):
                total += math.ceil(dist[i] / speed)
            total += dist[-1] / speed
            return total <= hour

        lo, hi = 1, 10**7

        while lo < hi:
            mid = (lo + hi) // 2
            
            if canReach(mid):
                hi = mid      # mid works, keep it in range (don't subtract 1)
            else:
                lo = mid + 1  # too slow, speed must be strictly greater than mid

        # When lo == hi, we have converged on the minimum valid speed
        return lo



        