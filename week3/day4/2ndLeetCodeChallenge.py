```python```
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        N = 0
        R = high
        L = low
        
        N = (R - L) // 2
 
        if (R % 2 != 0 or L % 2 != 0):
            N += 1
 
        return N
