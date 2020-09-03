'''Binary search
    Type: Search Algorithm 
    Category: Divide and Conqueor

    Serches a sorted array/list by dividing the search interval by half.


'''

def binary_search(t,key,low,high):

    if high>=low:
        mid = low + (high-low)//2

        if(t[mid] == key):
            return mid

        elif t[mid] >key:
            return binary_search(t,key,low,mid-1)
        elif t[mid]<key:
            return binary_search(t,key,mid+1,high)
    else:
        return -1




t = [23,34,21,23,54,23,5,7,234,56,23,456,34,67,48,25,16,36]
t.sort()
print(t)
print('\n')
low = 0
high = len(t)-1
key = input("enter the number to search for: ")
print("Index: ",binary_search(t,key,low,high))
