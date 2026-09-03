class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd_index = -1
        
        # Scan from left to right
        for i in range(len(num)):
            # Check if the current digit is odd
            if int(num[i]) % 2 != 0:
                last_odd_index = i  # Update to the latest position
                
        # If no odd digit was found
        if last_odd_index == -1:
            return ""
            
        # Return the substring up to the last odd digit
        return num[:last_odd_index + 1]
