import random
def partition(array, low, high):
    randpivot = random.randrange(low,high)
    (array[randpivot] , array[high]) = (array[high] , array[randpivot])
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

array = [-23, 0, 6, -4, 34, 101, -9, 0]
print("Before Sorting:", array)
quickSort(array,0,len(array)-1)
print("After Sorting: ", array)