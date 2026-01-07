class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Number of integers from low to high (inclusive)
        count = high - low + 1
        
        # If both low and high are odd, we have (count + 1) // 2 odd numbers
        # If either is odd, we have (count + 1) // 2 odd numbers  
        # If both are even, we have count // 2 odd numbers
        
        # Simplified: if either endpoint is odd, add 1 then divide by 2
        # Otherwise just divide by 2
        
        if low % 2 == 1 or high % 2 == 1:
            return (count + 1) // 2
        return count // 2