
def MergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[mid:]
        m = arr[:mid]
        MergeSort(l)
        MergeSort(m)

        i = j = k = 0

        while i<len(l) and j<len(m):
            if l[i] < m[j]:
                 arr[k]=l[i]
                 i+=1
            else:
                arr[k]=m[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1

        while j<len(m):
            arr[k]=m[j]
            j+=1
            k+=1


arr = [10, 7, 8, 2 , 6, 23] #random test cases
MergeSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
