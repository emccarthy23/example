import numpy as np
from example import algs

def test_bubblesort():
  #Empty vector
  x = []
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))

  #One entry
  x = [1]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))

  #Character entry
  x = ["a",1,2]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))

  #Non-integer entry
  x = [0.5,1,2]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))

  #Repeating entry (case 1)
  x = [6,1,3,6]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))
  #Repeating entry (case 2)
  x = [8,9,8,9]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))
  #Odd length entry
  x = [7,4,5]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))
  #Even length entry
  x = [7,4,5,1]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.bubblesort(x), sorted(x))
def test_quicksort():
  #Empty vector
  x = []
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))

  #One entry
  x = [1]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))

  #Character entry
  x = ["a",1,2]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))
  #Non-integer entry
  x = [0.5,1,2]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))
  #Repeating entry (case 1)
  x = [6,1,3,6]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))
  #Repeating entry (case 2)
  x = [8,9,8,9]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))
  #Odd length entry
  x = [7,4,5]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))
  #Even length entry
  x = [7,4,5,1]
  #check
  if algs.only_integers(x) == x:
    assert np.array_equal(algs.quicksort(x), sorted(x))

