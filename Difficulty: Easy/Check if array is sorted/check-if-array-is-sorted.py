class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n = len(arr)
        
        if n <= 1:
            return True
            
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                return False
                
        return True