# Input : arr[] = {100, 10, 5, 25, 35, 14}, n = 11
# Output : 9
# Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

def find_remainder(arr, n):
    temp = 1
    for number in arr:
        temp = number * temp
    print(temp % n)


arr = [100, 10, 5, 25, 35, 14]
n = 11
find_remainder(arr, n)
