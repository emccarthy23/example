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

def partition(x):
  lower_index=1
  higher_index=len(x)-1
  while higher_index > lower_index:
    while (x[lower_index] <= x[0]) & ((lower_index+1)<len(x)):
      lower_index = lower_index+1
    while (x[higher_index] > x[0]) & ((higher_index-1) > -1):
      higher_index = higher_index-1
    if higher_index > lower_index:
      x[higher_index],x[lower_index] = x[lower_index], x[higher_index]                                     
  return higher_index
      

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
      
    if (len(x) < 2):
        return x
    else:
        pivot=partition(x)
	if x[0] > x[pivot]:
          x[0], x[pivot] = x[pivot], x[0]
        return quicksort(x[:pivot]) + [x[pivot]] + quicksort(x[(pivot+1):])

