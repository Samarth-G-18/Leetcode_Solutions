class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        # Step A: Quick impossible check
        if len(bloomDay) < m * k:
            return -1

        # Step B: Helper function to validate a specific day guess
        def canMake(day):
            bouquets = 0
            count = 0
            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets >= m

        # Step C: Binary Search on Answer Space
        lo = min(bloomDay)
        hi = max(bloomDay)
        ans = -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if canMake(mid):
                ans = mid       # mid is a valid answer, but try finding an even smaller day
                hi = mid - 1
            else:
                lo = mid + 1    # not enough flowers, need more days

        return ans

        