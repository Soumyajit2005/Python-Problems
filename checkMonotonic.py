# Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j].

# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes).

def isMonotonic(A):
    value = False
    for i in range(1, len(A)):
        if(A[i - len(A)] <= A[i]) or A[i] >= A[i - len(A)]:
            value = True
    return value


# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))  # True
