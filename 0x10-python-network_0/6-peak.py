def findPeakUtil(arr, low, high, n):
  
    # Find index of middle element
    # low + (high - low) / 2
    mid = low + (high - low)/2
    mid = int(mid)
  
    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
  
  
    # If middle element is not peak and 
    # its left neighbour is greater 
    # than it, then left half must 
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
  
    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must 
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)

# A wrapper over recursive 
# function findPeakUtil()
# def findPeakWrapper(arr, n):
#     return findPeakUtil(arr, 0, n - 1, n)


# A Python program to find a peak element
# using divide and conquer
  
# A binary search based function
# that returns index of a peak element
# def findPeakWrapper(arr, n):
    
    l = 0
    r = n-1
      
    while(l <= r):
  
        # finding mid by binary right shifting.
        mid = (l + r) >> 1
  
        # first case if mid is the answer
        if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            break
  
        # move the right pointer
        if(mid > 0 and arr[mid - 1] > arr[mid]):
            r = mid - 1
  
        # move the left pointer
        else:
            l = mid + 1
  
    return mid



# A Python3 program to find a peak element
  
# Find the peak element in the array
def findPeakWrapper(arr, n) :
  
    # first or last element is peak element
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
   
    # check for every other element
    for i in range(1, n - 1) :
   
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i

def find_peak(list_of_integers):
    n = len(list_of_integers) - 1
    return findPeakWrapper(list_of_integers, n)