arr=[80,-50,90,100]
k=int(input("Enter K value"))

def consecutiveSum(arr,k,N):
    N=len(arr)
    max_sum=0
    for i in range(N-k+1):
        sum=0
        for j in range(i,k):
            sum+=arr[j]
        max_sum=max(max_sum,sum)
    return max_sum

print("Maximum Sum is %d"%consecutiveSum(arr,k,N))
