#Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing).
class Solution:

    def reverseSubArray(self, arr, l, r):
        def helper(arr, left, right):
            if left >= right:
                return
            arr[left], arr[right] = arr[right], arr[left]
            helper(arr, left + 1, right - 1)
        
        # Convert to 0-based indexing
        helper(arr, l - 1, r - 1)
        return arr


#Or 

class Solution:
    def reverseSubArray(self, arr, l, r):
        # Convert to 0-based indexing
        l -= 1
        r -= 1
        
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return arr
