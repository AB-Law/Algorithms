
def partition(arr,low,high):
    pivot = arr[high]
    print('\n Pivot:',pivot)
    i = low-1

    for j in range(low,high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)


def quickSort(arr,low,high):
    if(low<high):
        part = partition(arr, low ,high)
        for i in range(n):
            print ("%d" %arr[i])
        print('\n')

        quickSort(arr,low,part-1)
        quickSort(arr,part+1,high)

arr = [10, 7, 8, 2 , 6, 23] #random test cases
high = len(arr)
quickSort(arr,0,high-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
