class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i < j:
            # 2. Store the sum in a new variable instead of overwriting 'target'
            current_sum = numbers[i] + numbers[j]
            
            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                # 3. Return 1-based indices by adding 1 to both i and j
                return [i + 1, j + 1]
        
       
        
        