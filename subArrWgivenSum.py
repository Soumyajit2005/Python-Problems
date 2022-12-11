# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S and return the left and right index(1-based indexing) of that subarray.

# In case of multiple subarrays, return the subarray indexes which comes first on moving from left to right.

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       i = 0
       sum = 0
       while i<n:
           for item in self.arr[i:]:
               sum += item
            # if sum == s:
            #    return arr[i]
            # i = i+1

ob = Solution()
ob.subArraySum([1,2,3,7,5], 5, 12)


#Wrong code will fix it later