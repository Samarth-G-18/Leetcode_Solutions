class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity: int) -> bool:
            day_count = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    day_count += 1   # start a new day
                    current_load = 0
                current_load += w
            return day_count <= days
        
        lo, hi = max(weights), sum(weights)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if canShip(mid):
                hi = mid        # try smaller capacity
            else:
                lo = mid + 1    # need bigger capacity
        
        return lo
        