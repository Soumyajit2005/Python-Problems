# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
#Output:
# arr[] = [3, 4, 5, 6, 7, 1, 2]

def rotateArray(arr, d):
    return arr[d:] + arr[:d]




# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))