class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles) # Note: Some variants require max(piles) + 1 here
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Feasibility check inside the loop
            total_hours = sum((pile + mid - 1) // mid for pile in piles)
            
            if total_hours <= h:
                right = mid      # Move right to mid (keeps mid in the search space)
            else:
                left = mid + 1   # mid is invalid, so move past it
                
        return left  # At the end, left == right, pointing to the answer

        