class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # (2/21/25)(Fri)(352-356pm) done
        
        # regular method (also O(n) time and O(1) space):
#         n = len(nums)
#         expected_sum = n * (n+1) // 2
#         actual_sum = sum(nums)
#         return expected_sum - actual_sum
    
    
        # (2/21/25)(Fri)(356-400pm) done
        
        # Use XOR to do it in O(n) time and O(1) space:
        n = len(nums)
        missing = n
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing
        
        