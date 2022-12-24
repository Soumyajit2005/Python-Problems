# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S and return the left and right index(1-based indexing) of that subarray.

# In case of multiple subarrays, return the subarray indexes which comes first on moving from left to right.

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        sum = 0
        for i in range(n):
            sum = arr[i]
            if sum == s:
                return "The sum found at index " + str(i)
            else:
                for j in range(i+1,n):
                    sum += arr[j]
                    if sum == s:
                        return "The sum found between indexes",i+1,j+1
        return "No sub array found"
                    

ob = Solution()
print(ob.subArraySum([1,2,3,7,5], 5, 12)) #Output: 2, 4

arr = [15,2,4,8,9,5,10,23]
n = len(arr)
sum = 23
print(ob.subArraySum(arr, n, sum))  #Output: 2, 5