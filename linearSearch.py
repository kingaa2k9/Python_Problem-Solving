arr=[10,2,3,5,456,12,23]
target=int(input("Enter element to be searched"))




def linearSearch(arr,target):
    length=len(arr)
    for i in range(length):
        if (arr[i]==target):
            return i
    return -1
result=linearSearch(arr,target)

if result!=-1:
    print("Element found at %d location"%(result))
else:
    print("Element not found")
