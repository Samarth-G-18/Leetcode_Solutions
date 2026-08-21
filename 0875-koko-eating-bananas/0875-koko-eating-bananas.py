class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours needed at speed 'mid'
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                ans = mid       # Valid speed, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1   # Too slow, need faster speed
                
        return ans
        