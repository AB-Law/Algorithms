def BubbleSort(arr):
  n = len(arr)
  for j in range(0,n-1):
      for i in range(0,n-1):
          if(arr[i]>arr[i+1]):
              arr[i],arr[i+1]=arr[i+1],arr[i]

arr = [10, 7, 8, 2 , 6, 23] #random test cases
BubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
