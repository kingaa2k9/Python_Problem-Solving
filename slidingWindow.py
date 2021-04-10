arr=[80,-50,90,100]
k=3

def slidingWindow(arr,k):
    N=len(arr)
    sliding_sum=sum([arr[i] for i in range(0,k)])
    max_sum=sliding_sum
    for i in range(0,N-k):
        sliding_sum=sliding_sum-arr[i]+arr[i+k]
        max_sum=max(max_sum,sliding_sum)

    return max_sum


print(slidingWindow(arr,k))
