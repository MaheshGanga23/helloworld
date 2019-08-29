# Program for implementation of Bubble Sort

def bubble_sort(arr):
  '''Sorting given array
    Args<List>: arr should be list.
  
  '''
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if arr[j]> arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True

  # If not swapped, that means the list has already sorted.
  if not swapped:
    break
    

#generate array with random numbers.
import random
a = [] 
for i in range(1, 10):
  a.append(random.randint(0, 60))
  
#now a is a list of 10 items, between 0 to 60. ex: [28, 6, 2, 32, 42, 17, 31, 40, 36]
# if array is already sorted, use following code to shuffle the list, 
#random.shuffle(a)

# now pass the array to above function(bubble_sort)
bubble_sort(a)
print (a)

output:
[2, 6, 17, 28, 31, 32, 36, 40, 42]





