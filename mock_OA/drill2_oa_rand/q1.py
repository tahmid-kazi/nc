class Solution:
    
    # (2/21/25)(Fri)(237-240pm) done
    
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(heights[i] != expected[i] for i in range(len(heights)))