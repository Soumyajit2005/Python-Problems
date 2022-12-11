# Input : arr[] = {10, 20, 4}
# Output : 20

# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100
#........................................................................................
# Python3 program to find maximum
# in arr[] of size n
 
# python function to find maximum
# in arr[] of size n

def largest_value(arr):
    largest_element = 0
    for item in arr:
        if item >= largest_element:
            largest_element = item
        else:
            continue
    return largest_element

arr = [10, 324, 45, 90, 9808]
Ans = largest_value(arr)
print("Largest in given array ", Ans)