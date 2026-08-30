import math
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to check if a maximum load of 'mid' per store is feasible
        def can_distribute(mid: int) -> bool:
            stores_needed = 0
            for q in quantities:
                # Calculate ceil(q / mid) using integer arithmetic
                stores_needed += (q + mid - 1) // mid
            return stores_needed <= n

        # Binary search range
        low = 1
        high = max(quantities)
        result = high

        while low <= high:
           # standard mid point
            mid = low + (high - low) // 2
            
            if can_distribute(mid):
                result = mid      # mid is a feasible answer, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1     # mid is too small, increase the capacity
                
        return result





        