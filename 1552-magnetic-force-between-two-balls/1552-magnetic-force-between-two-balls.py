class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()  # Positions must be sorted first
        
        def can_place(dist: int) -> bool:
            # Helper: Can we place 'm' balls with at least 'dist' space between them?
            count = 1
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= dist:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                ans = mid        # Valid separation, try to maximize it
                left = mid + 1
            else:
                right = mid - 1  # Distance too large, decrease it
                
        return ans
        
        