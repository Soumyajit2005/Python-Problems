#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]

#Input : [1, 2, 3]
#Output : [3, 2, 1]

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    temp = newList[0]
    newList[0] = newList[len(newList)-1]
    newList[len(newList)-1] = temp
    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
