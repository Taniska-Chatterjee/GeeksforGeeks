class Solution:
    def largest(self, arr):
        # code here
        largest_element = arr[0]
        
        for i in arr:
            if i > largest_element:
                largest_element = i
        
        return largest_element
