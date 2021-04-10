arr=[10,230,465,876,7,12,2,34235,1]
# arr=[1,2,3,4,5,6,7,8,9,10]

target=int(input())

arr.sort()

def binarySearch(arr,target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            return mid
        elif(target<arr[mid]):
            right=mid-1
        else:
            left=mid+1
    return -1
            
        






result=binarySearch(arr,target)
if(result!=-1):
    print("Element found at %d location"%result)
else:
    print("Element not found")

