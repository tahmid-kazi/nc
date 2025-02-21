class Solution:
    
    # (2/21/25)(Fri)(340-346pm) done
    
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # use 2 pointer approach
        
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                j += 1
                i += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return i == len(name)
        