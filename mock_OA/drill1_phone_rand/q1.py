class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # (2/21/25) (Fri) (1014-1032am) done 
        
        # first sort the array (so that you can find the min absolute distance in the first pass)
        arr.sort()
        full_arr = []
        

        # find the min absolute difference first
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i]-arr[i-1]
            min_diff = min(diff, min_diff)
        
        for i in range(1, len(arr)):
            diff = arr[i]-arr[i-1]
            if diff == min_diff:
                full_arr.append([arr[i-1], arr[i]])
        
        return full_arr