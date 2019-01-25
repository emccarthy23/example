import numpy as np

def bubblesort(x):
  """
  Describe how you are sorting `x`:
  Start at the beginning of the list and for each pair of elements
  i and i+1 flip the order if i+1 is smaller than i.
  Iterate over the list pairwise until the list is sorted.
  """
  try: 
    test = [i == int(i) for i in x]
    if sum(test)!=len(x):
      return "Please provide a list made ONLY of integers."
  except ValueError:
    return 'Please provide a list made ONLY of integers.'
  if (len(x) > 1):
    j=1
    while j!=0:
      j=0
      for i in range(len(x)-1):    
        if x[i] > x[i+1]:
          x[i],x[i+1] = x[i+1],x[i]
          j = j+1
    return x
  else:
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    Choose a pivot. Arrange all the elements so the larger elements are in front of the pivot
    and the smaller elements are behind the pivot. Then recursively apply the funciton on the sublists.
    """
    try: 
        test = [i == int(i) for i in x]
        if sum(test)!=len(x):
            return "Please provide a list made ONLY of integers."
    except ValueError:
        return 'Please provide a list made ONLY of integers.'
    quicksort_recursive(x,0,len(x)-1)
    return x
    


def quicksort_recursive(x,low,high):
    if high > low:

        pivot = partition(x,low,high)
        quicksort_recursive(x,low,pivot-1)
        quicksort_recursive(x,pivot+1,high)

        
def partition(x,low,high):
    
    middle = x[low]
    lower_index = low
    higher_index = high
    
    while higher_index > lower_index:
        
        while lower_index <= higher_index and x[lower_index] <= middle:
            lower_index = lower_index + 1
            
        while x[higher_index] >= middle and higher_index >= lower_index:
            higher_index = higher_index - 1
            
        if higher_index > lower_index:
            x[higher_index],x[lower_index] = x[lower_index],x[higher_index]
            
    x[low],x[higher_index] = x[higher_index],middle
    
    return higher_index
