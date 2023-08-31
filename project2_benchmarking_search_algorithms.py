from random import seed, sample
import math

def make_data(data_size):#DO NOT REMOVE OR MODIFY THIS FUNCTION
    '''A generator for producing data_size random values
    '''
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data


def linear_search(lyst, target):
    # Added variable to hold total number of comparisons.
    comparisons = 0
   
    for i in range(len(lyst)):
        comparisons = comparisons + 1
        if (lyst[i] == target):
           return True, comparisons
    return False, comparisons # not found


def binary_search(lyst, target):
    # Added variable to hold total number of comparisons.
    comparisons = 0

    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts at whole range
    low = 0
    mid = len(lyst) // 2
    high = len(lyst) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # Calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        comparisons = comparisons + 1
        if (lyst[mid] < target):
            low = mid + 1
      
        elif (lyst[mid] > target):
            high = mid - 1
      
        else:
            return True, comparisons
  
    return False, comparisons # not found
            






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
            return False,occurance
     
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

def main():
    lyst = [2, 4, 7, 10, 11, 32, 45, 87]
    print('NUMBERS:', lyst)
        
    target = int(input('Enter an integer key to search for: '))
    print(f'target is {target}')
    
    # Test linear search
    bool, comparisons = linear_search(lyst, target)
    print(bool, comparisons)      
    # if (key_index == -1):
    #     print('Linear search: %d was not found with %d comparisons.' % (target, comparisons))
    # else:
    #     print('Linear search: Found %d at index %d with %d comparisons.' % (target, key_index, comparisons))
    index, comparisons = binary_search(lyst, target)
    print(index, comparisons)

    jump_bool, jump_comparison = jumpSearch(lyst, target)
    print(f"{jump_bool} {jump_comparison}")
if __name__ == "__main__":
    main()