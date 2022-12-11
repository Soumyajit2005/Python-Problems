# Input : arr[] = {1, 2, 3}
# Output : 6
# 1 + 2 + 3 = 6

# Input : arr[] = {15, 12, 13, 10}
# Output : 50

# Python 3 code to find sum
# of elements in given array

def sum(arr):
    sum = 0;
    for items in arr:
        sum += items

    return sum

# input values to list
arr = [12, 3, 4, 15]
 
ans = sum(arr)
 
# display sum
print('Sum of the array is ', ans)