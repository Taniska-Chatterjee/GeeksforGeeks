class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest_element = -1
        second_largest = -1
        
        for num in arr:
            
            if num > largest_element:
                second_largest = largest_element
                largest_element = num
                
            elif num < largest_element and num > second_largest:
                second_largest = num
                
        return second_largest