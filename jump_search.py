# Python3 code to implement Jump Search
import math
 
def jumpSearch( lyst , target):
    n = len(lyst)
    occurance = 0
    # Finding block size to be jumped
    step = math.sqrt(n)
     
    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while lyst[int(min(step, n)-1)] < target:
        occurance = occurance + 1
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return True,occurance
     
    # Doing a linear search for x in
    # block beginning with prev.
    while lyst[int(prev)] < target:
        occurance = occurance + 1
        prev += 1
         
        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return False,occurance
     
    # If element is found
    if lyst[int(prev)] == target:
        occurance = occurance + 1
        return True,occurance
     
    return False,occurance
 
# Driver code to test function
lyst = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
print(lyst)
target = int(input("Pick a target: "))


# Find the index of 'x' using Jump Search
index, occurance = jumpSearch(lyst, target)
 
# Print the index where 'x' is located
print(f"{index} with occurance of {occurance}")